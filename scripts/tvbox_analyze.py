#!/usr/bin/env python3
"""TVBox 订阅源一键分析脚本（skill 主脚本）

流程：抓取源列表(HTML) → 每源连测2次取平均 → 健壮解析 → 特征校验+质量过滤 → tab分级(内部参考) → 输出

产出：
- <outdir>/urls.md   —— 交付用户：仅有效源完整 URL 列表（一行一个，可直接复制）
- <outdir>/report.md —— agent 内部参考：tab 分级、类型分布、剔除原因（勿发给用户）

用法：
  python3 tvbox_analyze.py --outdir /tmp/tvbox-analysis [--source-url URL] [--timeout 15] [--workers 6]
"""
import argparse
import base64
import concurrent.futures as cf
import html as html_mod
import json
import os
import re
import ssl
import time
import urllib.parse
import urllib.request
from collections import Counter

DEFAULT_SOURCE = 'https://tvbox.wpcoder.cn/user.php'
UA = 'Mozilla/5.0 (TVBox)'
TVBOX_KEYS = ('sites', 'spider', 'lives', 'parses', 'rules', 'danmaku', 'flags')
DEAD_HINTS = ('失效', '已停', '过期', '无法使用', '已下线', '停用', '链接已')
NO_CAT_CSP = ('csp_Douban', 'csp_DouDou')
GUARD_CSP = ('Guard',)

# 兜底源列表（源列表页抓不到时使用，2026-08 实测有效的源）
FALLBACK_SOURCES = [
    ('11_liu673cn', 'https://cdn.jsdelivr.net/gh/liu673cn/box@main/m.json'),
    ('ok_liucn', 'https://raw.liucn.cc/box/m.json'),
    ('拾光_svip', 'https://gh-proxy.com/https://raw.githubusercontent.com/xmbjm/svip/refs/heads/main/svip.json'),
    ('神秘大佬_jsm', 'https://g.33445500.xyz/https://raw.githubusercontent.com/qist/tvbox/refs/heads/master/jsm.json'),
    ('小苹果_xpg', 'https://bitbucket.org/xduo/duoapi/raw/master/xpg.json'),
    ('金鹰_550', 'http://550.3vcn.work/wdjyys.json'),
    ('小盒子4K', 'http://xhztv.top/4k.json'),
    ('荐片_0821', 'https://tv.203511.xyz/0821.json'),
    ('cs_nxog', 'http://tv.nxog.top/m/'),
    ('1_vip', 'https://700sjro44343.vicp.fun/vip/vip/tv.json'),
    ('二月红_0211', 'https://700sjro44343.vicp.fun/eggp/0211/tv.json'),
    ('潇洒_qist', 'https://qist.wyfc.qzz.io/xiaosa/api.json'),
    ('潇洒_g334', 'https://g.33445500.xyz/https://raw.githubusercontent.com/qist/tvbox/refs/heads/master/xiaosa/api.json'),
    ('摸鱼儿_fish', 'https://6800.kstore.vip/fish.json'),
    ('软件_47', 'http://47.96.82.41:5188/api.json'),
    ('my_124', 'http://124.223.214.31:8/api.json'),
    ('fmys', 'http://fmys.top/fmys.json'),
    ('俊哥_jundie', 'http://home.jundie.top:81/top98.json'),
    ('xn6', 'http://xn--6orr3pi6g9uu.top/'),
    ('饭太硬_fty', 'https://qist.wyfc.qzz.io/fty.json'),
    ('王二小', 'https://9280.kstore.vip/newwex.json'),
    ('牛儿', 'https://9280.kstore.space/wex.json'),
    ('牛二', 'https://9280.kstore.space/newwex.json'),
]

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# ---------- 源列表抓取 ----------

def load_sources(source_url):
    """从 HTML 表格提取 (name, url) 列表；失败则用兜底源"""
    items = []
    try:
        req = urllib.request.Request(source_url, headers={'User-Agent': UA})
        body = urllib.request.urlopen(req, timeout=20, context=ctx).read()
        text = body.decode('utf-8', errors='ignore')
        rows = re.findall(r'<tr[^>]*>(.*?)</tr>', text, re.S)
        for row in rows:
            name_m = re.search(r'<td[^>]*class="td-name"[^>]*>(.*?)</td>', row, re.S)
            if not name_m:
                continue
            name = html_mod.unescape(re.sub(r'<[^>]+>', '', name_m.group(1)).strip())
            urls = re.findall(r'https?://[^"<>()\s\\]+', row)
            urls = [re.sub(r'&amp;', '&', u).rstrip('.,;') for u in urls]
            urls = [u for u in urls if not any(x in u.lower() for x in ['example.com', 'googlesyndication.com', 'pan.wpcoder.cn'])]
            for u in urls:
                items.append({'name': name, 'url': u})
    except Exception as e:
        print(f'[warn] 源列表页抓取失败: {e}，使用兜底源')
    if not items:
        items = [{'name': n, 'url': u} for n, u in FALLBACK_SOURCES]
    # 去重
    seen, uniq = set(), []
    for it in items:
        if it['url'] not in seen:
            seen.add(it['url'])
            uniq.append(it)
    return uniq


# ---------- 请求 ----------

def quote_url(url):
    """对含非 ASCII 的 URL 做规范化：主机名 IDNA(punycode)，路径 percent-encode。
    否则 urllib 会抛 'latin-1' codec 错误；规范化后即使域名不存在也只返回 DNS 失败。"""
    try:
        url.encode('ascii')
        return url
    except UnicodeEncodeError:
        pass
    try:
        parts = urllib.parse.urlsplit(url)
        netloc = parts.netloc.encode('idna').decode('ascii') if parts.netloc else ''
        path = urllib.parse.quote(parts.path or '/', safe="/:@!$&'()*+,;=~")
        query = urllib.parse.quote(parts.query or '', safe="?:@!$&'()*+,;=~%")
        return urllib.parse.urlunsplit((parts.scheme, netloc, path, query, parts.fragment))
    except Exception:
        # IDNA/拆分失败时退化为纯 percent-encode，保证不抛编码异常
        return urllib.parse.quote(url, safe=':/?#[]@!$&\'()*+,;=%')

def fetch(url, timeout=15):
    """返回 (耗时, 状态/错误, body, 最终URL)。自动跟随重定向。"""
    t0 = time.time()
    try:
        req = urllib.request.Request(quote_url(url), headers={'User-Agent': UA, 'Accept': '*/*'})
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            body = resp.read(500000)
            return time.time() - t0, resp.status, body, resp.geturl()
    except Exception as e:
        return time.time() - t0, str(e)[:60], b'', url


# ---------- 健壮解析 ----------

def strip_jsonc(text):
    """剥离字符串外的 // 注释（状态机，跳过 \\ 转义与字符串）"""
    out, i, n, in_str = [], 0, len(text), False
    while i < n:
        c = text[i]
        if c == '\\' and i + 1 < n:
            out.append(c); out.append(text[i + 1]); i += 2
            continue
        if c == '"':
            in_str = not in_str; out.append(c); i += 1
            continue
        if not in_str and c == '/' and i + 1 < n and text[i + 1] == '/':
            while i < n and text[i] != '\n':
                i += 1
            continue
        out.append(c); i += 1
    return ''.join(out)


def process(text):
    """把字符串内未转义的控制字符(\r\n\t)转义为字面 \\r\\n\\t
    注意：dict 的 key 必须是真实控制字符（单个字符 \n），不是 '\\n' 两字符"""
    out, i, n, in_str = [], 0, len(text), False
    esc = {'\n': '\\n', '\r': '\\r', '\t': '\\t'}
    while i < n:
        c = text[i]
        if c == '\\' and i + 1 < n:
            out.append(c); out.append(text[i + 1]); i += 2
            continue
        if c == '"':
            in_str = not in_str; out.append(c); i += 1
            continue
        if in_str and c in esc:
            out.append(esc[c]); i += 1
            continue
        out.append(c); i += 1
    return ''.join(out)


def try_base64(text):
    s = text.strip()
    if len(s) < 10:
        return None
    s_clean = re.sub(r'\s+', '', s)
    if not re.fullmatch(r'[A-Za-z0-9+/=]+', s_clean) or len(s_clean) % 4 != 0:
        return None
    try:
        dec = base64.b64decode(s_clean, validate=True).decode('utf-8', errors='ignore')
        if '{' in dec and any(k in dec for k in ('"sites"', '"spider"', '"lives"')):
            return dec
    except Exception:
        pass
    return None


def parse_json_robust(text):
    """逐层尝试: direct -> bracket -> jsonc -> base64"""
    text = text.lstrip('\ufeff')
    for attempt in ('direct', 'bracket', 'jsonc', 'base64'):
        try:
            if attempt == 'direct':
                data = json.loads(text)
            elif attempt == 'bracket':
                start, end = text.index('{'), text.rindex('}') + 1
                data = json.loads(text[start:end])
            elif attempt == 'jsonc':
                cleaned = strip_jsonc(text)
                fixed = process(cleaned)
                start, end = fixed.index('{'), fixed.rindex('}') + 1
                data = json.loads(fixed[start:end])
            elif attempt == 'base64':
                dec = try_base64(text)
                data = json.loads(dec) if dec else None
            if isinstance(data, dict):
                return data
        except Exception:
            data = None
    return None


def parse_sites_fallback(text):
    """整体解析失败时：逐对象 raw_decode 提取 sites"""
    fixed = process(strip_jsonc(text))
    m = re.search(r'"sites"\s*:\s*\[(.*)\]', fixed, re.S)
    if not m:
        return None
    arr_text = '[' + m.group(1) + ']'
    dec = json.JSONDecoder()
    idx, n, sites = 0, len(arr_text), []
    while idx < n:
        while idx < n and arr_text[idx] in ' \t\r\n,':
            idx += 1
        if idx >= n or arr_text[idx] == ']':
            break
        try:
            obj, idx = dec.raw_decode(arr_text, idx)
            if isinstance(obj, dict):
                sites.append(obj)
        except json.JSONDecodeError:
            idx = arr_text.find('{', idx + 1)
            if idx == -1:
                break
    return {'sites': sites} if sites else None


# ---------- 聚合页解析（link3 名片页 / 多仓文件） ----------

LINK3_API = 'https://v5.api.link3.cc:5678/api/no_auth/user'

def is_link3_page(text):
    """检测是否为 link3 聚合页（数字名片），特征：meta description 或关键字"""
    if not text:
        return False
    return ('link3' in text.lower() and '聚合链接' in text) or ('link3.cc' in text.lower() and '数字名片' in text)


def extract_link3_username(url):
    """从 URL 提取 link3 用户名：https://link3.cc/uuccc -> uuucc"""
    m = re.search(r'link3\.cc/([a-zA-Z0-9_\-]+)', url)
    return m.group(1) if m else None


def fetch_link3_links(username):
    """调用 link3 API 获取该用户页面的全部链接，返回 [{'title','url'}]"""
    if not username:
        return []
    try:
        body = json.dumps({'username': username}).encode('utf-8')
        req = urllib.request.Request(LINK3_API, data=body, headers={
            'User-Agent': UA, 'Content-Type': 'application/json',
            'Origin': 'https://link3.cc', 'Referer': 'https://link3.cc/'})
        resp = urllib.request.urlopen(req, timeout=15, context=ctx)
        data = json.loads(resp.read().decode('utf-8', errors='ignore'))
        d = data.get('data', {}) if isinstance(data, dict) else {}
        links_raw = d.get('links', [])
        if isinstance(links_raw, str):
            try:
                links_raw = json.loads(links_raw)
            except Exception:
                return []
        out = []
        for link in links_raw if isinstance(links_raw, list) else []:
            if not isinstance(link, dict):
                continue
            tv = link.get('typeValue', {})
            if isinstance(tv, str):
                try:
                    tv = json.loads(tv)
                except Exception:
                    tv = {}
            if not isinstance(tv, dict):
                continue
            title = tv.get('title', '')
            # text 类型内容在 content，url 类型在 nav_url
            val = tv.get('content', '') or tv.get('nav_url', '')
            if isinstance(val, str) and val.startswith('http'):
                out.append({'title': title, 'url': val})
        return out
    except Exception as e:
        print(f'  [link3 API] {username} 解析失败: {str(e)[:50]}')
        return []


def is_multi_store_file(text):
    """检测是否为多仓文件：顶层有 urls 数组（每项含 url 字段），无 sites"""
    try:
        data = json.loads(text)
        return isinstance(data, dict) and isinstance(data.get('urls'), list) and 'sites' not in data
    except Exception:
        return False


def extract_multi_store_urls(text):
    """从多仓文件提取 url 列表，返回 [{'title','url'}]"""
    out = []
    try:
        data = json.loads(text)
        for item in data.get('urls', []):
            if isinstance(item, dict):
                u = item.get('url', '')
                if isinstance(u, str) and u.startswith('http'):
                    out.append({'title': item.get('name', ''), 'url': u})
    except Exception:
        pass
    return out


def expand_aggregate(url, body, final_url):
    """对非 TVBox 的响应尝试聚合页展开，返回 [{'title','url'}] 候选子源"""
    text = body.decode('utf-8', errors='ignore').lstrip('\ufeff') if body else ''
    # 1) link3 聚合页
    if is_link3_page(text) or 'link3.cc/' in final_url:
        username = extract_link3_username(final_url)
        return fetch_link3_links(username)
    # 2) 多仓文件
    if is_multi_store_file(text):
        return extract_multi_store_urls(text)
    return []


# ---------- 校验 ----------

def validate(body):
    """返回 (is_valid, detail)"""
    if not body:
        return False, '空内容'
    text = body.decode('utf-8', errors='ignore').lstrip('\ufeff')
    data = parse_json_robust(text)
    if not isinstance(data, dict):
        # 宽松特征检测
        if re.search(r'"sites"\s*:\s*\[', text) or re.search(r'"spider"\s*:', text) or re.search(r'"lives"\s*:', text):
            api_count = len(re.findall(r'"api"\s*:', text))
            if api_count >= 3:
                return True, f'宽松有效(JSON解析失败但特征齐全) sites含api约{api_count}个'
            return False, f'含特征但内容不完整(api字段{api_count}个): {text[:50]}'
        return False, f'非TVBox: {text[:50]}'

    hit_keys = [k for k in TVBOX_KEYS if k in data]
    sites = data.get('sites')
    spider = data.get('spider', '')
    # spider 指向图片：仅当无真实站点时才视为失效替换标记（王二小等源 spider 用图片占位但 sites 有效）
    spider_is_img = isinstance(spider, str) and re.search(r'\.(png|jpg|jpeg|gif|webp)([?;]|$)', spider.lower())
    if isinstance(sites, list) and len(sites) > 0:
        # 非失效提示且带 api 的站点数；若全是失效提示站点则剔除
        real_sites = 0
        dead_sites = 0
        for s in sites:
            if not isinstance(s, dict):
                continue
            sname = str(s.get('name', ''))
            if any(h in sname for h in DEAD_HINTS):
                dead_sites += 1
            elif s.get('api'):
                real_sites += 1
        if dead_sites >= len(sites) and real_sites == 0:
            return False, f'sites全是失效提示: "{sites[0].get("name","")[:30] if sites else ""}"'
        valid_api = sum(1 for s in sites if isinstance(s, dict) and s.get('api'))
        return True, f'sites={len(sites)}个(有效api:{valid_api})'
    # 无 sites 列表
    if spider_is_img:
        return False, f'spider指向图片且无sites(失效标记): {spider[:60]}'
    if hit_keys:
        n_lives = len(data.get('lives', [])) if isinstance(data.get('lives'), list) else '?'
        return True, f'无sites列表, lives={n_lives} {hit_keys}'
    return False, f'JSON有效但无TVBox内容 keys={list(data.keys())[:8]}'


def test_twice(it, timeout):
    r1 = fetch(it['url'], timeout)
    r2 = fetch(it['url'], timeout)
    avg = (r1[0] + r2[0]) / 2
    status1, status2 = r1[1], r2[1]
    body = r2[2] if r2[1] == 200 else r1[2]
    ok_http = status1 == 200 and status2 == 200
    valid, detail = validate(body)
    return {**it, 'avg': avg, 'ok': ok_http and valid, 'http': f'{status1}/{status2}',
            'r1': r1[0], 'r2': r2[0], 'detail': detail or '', 'final_url': r2[3], 'body': body}


# ---------- tab 分级（内部参考） ----------

def classify_site(s):
    if not isinstance(s, dict):
        return 'unknown'
    t = s.get('type')
    api = str(s.get('api', ''))
    if s.get('categories'):
        return 'A_cat'
    if t == 1 and api:
        return 'type1'
    if t == 3 and api.startswith('csp_'):
        if api in NO_CAT_CSP:
            return 'D_nocat'
        if any(g in api for g in GUARD_CSP):
            return 'C_guard'
        return 'B_csp'
    if t == 3 and api:
        return 'B_drpy'
    return 'other'


def test_type1(api):
    if not api:
        return 'no-api'
    try:
        req = urllib.request.Request(api, headers={'User-Agent': UA})
        body = urllib.request.urlopen(req, timeout=8, context=ctx).read(30000)
        text = body.decode('utf-8', errors='ignore')
        if '"class"' in text or '"list"' in text:
            return '✅分类OK'
        if '<class' in text.lower() or 'type' in text.lower():
            return '✅xml分类'
        return f'⚠️可访问({len(text)}B)'
    except Exception as e:
        return f'❌{str(e)[:25]}'


def analyze_tab(data, name, url):
    """返回 (level, detail)；level 仅内部参考"""
    if not data or not data.get('sites'):
        return '❌解析失败', '-'
    sites = data['sites']
    if not isinstance(sites, list) or len(sites) == 0:
        return '❌无sites', '-'
    cats = Counter()
    type1_sites = []
    for s in sites:
        k = classify_site(s)
        cats[k] += 1
        if k == 'type1':
            type1_sites.append(s)
    if cats.get('A_cat', 0) > 0:
        level = 'A-必有tab'
    elif type1_sites and any('✅' in test_type1(s.get('api')) for s in type1_sites[:3]):
        level = 'A-必有tab'
    elif cats.get('B_csp', 0) + cats.get('B_drpy', 0) > 0:
        level = 'B-大概率tab'
    elif cats.get('C_guard', 0) > 0:
        level = 'C-存疑'
    elif cats.get('D_nocat', 0) > 0:
        level = 'D-无tab'
    else:
        level = '?'
    detail = (f"A_cat={cats.get('A_cat',0)} type1={cats.get('type1',0)} "
              f"csp={cats.get('B_csp',0)} drpy={cats.get('B_drpy',0)} "
              f"guard={cats.get('C_guard',0)} 豆瓣类={cats.get('D_nocat',0)}")
    return level, detail


# ---------- 主流程 ----------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--outdir', default='/tmp/tvbox-analysis')
    ap.add_argument('--source-url', default=DEFAULT_SOURCE)
    ap.add_argument('--timeout', type=float, default=15)
    ap.add_argument('--workers', type=int, default=6)
    args = ap.parse_args()
    os.makedirs(args.outdir, exist_ok=True)

    uniq = load_sources(args.source_url)
    print(f"共 {len(uniq)} 个订阅源，拉取真实内容校验(连测2次取平均)...\n")

    results = []
    with cf.ThreadPoolExecutor(max_workers=args.workers) as ex:
        for r in ex.map(lambda it: test_twice(it, args.timeout), uniq):
            results.append(r)

    # 聚合页展开：对非 TVBox 但命中 link3/多仓 形态的失败源，尝试解析出子源再测
    expanded = []
    expanded_urls = set()
    for r in results:
        if r['ok'] or not r['body']:
            continue
        try:
            subs = expand_aggregate(r['url'], r['body'], r['final_url'])
        except Exception:
            subs = []
        for s in subs:
            if s['url'] not in expanded_urls:
                expanded_urls.add(s['url'])
                expanded.append({'name': f"{r['name']}/{s['title']}", 'url': s['url'], 'parent': r['url']})
        if subs:
            print(f"  聚合页 {r['name']} -> 展开 {len(subs)} 个子链接")
    if expanded:
        with cf.ThreadPoolExecutor(max_workers=args.workers) as ex:
            for rr in ex.map(lambda it: test_twice(it, args.timeout), expanded):
                results.append(rr)

    ok_list = sorted([r for r in results if r['ok']], key=lambda x: x['avg'])
    fail_list = sorted([r for r in results if not r['ok']], key=lambda x: x['avg'])

    # tab 分级（内部参考，需真实内容）
    tab_info = {}
    for r in ok_list:
        try:
            text = r['body'].decode('utf-8', errors='ignore').lstrip('\ufeff')
            data = parse_json_robust(text) or parse_sites_fallback(text)
            level, detail = analyze_tab(data, r['name'], r['url'])
            tab_info[r['url']] = (level, detail)
        except Exception:
            tab_info[r['url']] = ('?', '-')

    # 排序：A级优先，然后平均耗时
    level_rank = {'A-必有tab': 0, 'B-大概率tab': 1, 'C-存疑': 2, 'D-无tab': 3}
    ok_list.sort(key=lambda r: (level_rank.get(tab_info.get(r['url'], ('?', '-'))[0], 9), r['avg']))

    # urls.md —— 交付用户：仅完整 URL
    with open(os.path.join(args.outdir, 'urls.md'), 'w', encoding='utf-8') as f:
        for r in ok_list:
            f.write(f"{r['url']}\n")

    # report.md —— 内部参考
    with open(os.path.join(args.outdir, 'report.md'), 'w', encoding='utf-8') as f:
        f.write("# TVBox 订阅源分析报告（agent 内部参考，勿交付用户）\n\n")
        f.write(f"数据源: {args.source_url}\n\n")
        f.write("## ✅ 有效源（含 tab 分级）\n\n")
        f.write("| # | 名称 | tab级别 | 平均耗时 | 两次耗时 | 内容校验 | URL |\n")
        f.write("|:-:|------|:------:|:------:|:------:|---------|-----|\n")
        for i, r in enumerate(ok_list, 1):
            level, detail = tab_info.get(r['url'], ('?', '-'))
            f.write(f"| {i} | {r['name']} | {level} | {r['avg']:.3f}s | {r['r1']:.2f}/{r['r2']:.2f} | {detail} | `{r['url']}` |\n")
        f.write("\n## ❌ 无效/失败\n\n")
        f.write("| 接口名称 | 平均耗时 | HTTP | 原因 | URL |\n")
        f.write("|:-------:|:------:|:----:|------|-----|\n")
        for r in fail_list:
            f.write(f"| {r['name']} | {r['avg']:.3f}s | {r['http']} | {r['detail']} | `{r['url']}` |\n")

    # sources.json —— 网页用：名称 + URL + tab级别
    level_map = {'A-必有tab': 'A', 'B-大概率tab': 'B', 'C-存疑': 'C', 'D-无tab': 'D', '?': 'B'}
    with open(os.path.join(args.outdir, 'sources.json'), 'w', encoding='utf-8') as f:
        items = []
        for r in ok_list:
            level, _ = tab_info.get(r['url'], ('?', '-'))
            items.append({'name': r['name'], 'url': r['url'], 'level': level_map.get(level, 'B')})
        json.dump(items, f, ensure_ascii=False, indent=2)

    # stdout —— 最终交付摘要
    print("=" * 100)
    print(f"✅ 真实有效 TVBox 接口 {len(ok_list)} 个")
    print("=" * 100)
    for i, r in enumerate(ok_list, 1):
        level, detail = tab_info.get(r['url'], ('?', '-'))
        print(f"{i}. [{r['name']}] {level} {r['avg']:.3f}s")
        print(f"   {r['url']}")
    print()
    print(f"❌ 无效/失败 {len(fail_list)} 个")
    for r in fail_list:
        print(f"- [{r['name']}] {r['avg']:.3f}s HTTP:{r['http']} {r['detail'][:60]}")
    print()
    print(f"交付文件: {os.path.join(args.outdir, 'urls.md')}")
    print(f"内部参考: {os.path.join(args.outdir, 'report.md')}")


if __name__ == '__main__':
    main()
