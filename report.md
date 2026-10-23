# TVBox 订阅源分析报告（agent 内部参考，勿交付用户）

数据源: https://tvbox.wpcoder.cn/user.php

## ✅ 有效源（含 tab 分级）

| # | 名称 | tab级别 | 平均耗时 | 两次耗时 | 内容校验 | URL |
|:-:|------|:------:|:------:|:------:|---------|-----|
| 1 | 11_liu673cn | A-必有tab | 0.041s | 0.05/0.03 | A_cat=11 type1=4 csp=164 drpy=54 guard=0 豆瓣类=1 | `https://cdn.jsdelivr.net/gh/liu673cn/box@main/m.json` |
| 2 | 荐片_0821 | A-必有tab | 0.089s | 0.11/0.07 | A_cat=3 type1=2 csp=2 drpy=21 guard=0 豆瓣类=0 | `https://tv.203511.xyz/0821.json` |
| 3 | 拾光_svip | A-必有tab | 0.130s | 0.17/0.09 | A_cat=24 type1=8 csp=135 drpy=77 guard=0 豆瓣类=1 | `https://gh-proxy.com/https://raw.githubusercontent.com/xmbjm/svip/refs/heads/main/svip.json` |
| 4 | 神秘大佬_jsm | A-必有tab | 0.202s | 0.32/0.08 | A_cat=8 type1=7 csp=104 drpy=34 guard=0 豆瓣类=0 | `https://g.33445500.xyz/https://raw.githubusercontent.com/qist/tvbox/refs/heads/master/jsm.json` |
| 5 | 小盒子4K | A-必有tab | 0.209s | 0.21/0.21 | A_cat=6 type1=3 csp=37 drpy=6 guard=0 豆瓣类=1 | `http://xhztv.top/4k.json` |
| 6 | ok_liucn | A-必有tab | 0.210s | 0.39/0.03 | A_cat=11 type1=4 csp=164 drpy=54 guard=0 豆瓣类=1 | `https://raw.liucn.cc/box/m.json` |
| 7 | 金鹰_550 | A-必有tab | 1.686s | 1.88/1.49 | A_cat=14 type1=0 csp=79 drpy=7 guard=0 豆瓣类=1 | `http://550.3vcn.work/wdjyys.json` |
| 8 | 饭太硬_fty | B-大概率tab | 0.077s | 0.07/0.08 | A_cat=0 type1=0 csp=0 drpy=3 guard=46 豆瓣类=0 | `https://qist.wyfc.qzz.io/fty.json` |
| 9 | 潇洒_g334 | B-大概率tab | 0.105s | 0.13/0.08 | A_cat=0 type1=0 csp=104 drpy=2 guard=0 豆瓣类=1 | `https://g.33445500.xyz/https://raw.githubusercontent.com/qist/tvbox/refs/heads/master/xiaosa/api.json` |
| 10 | 潇洒_qist | B-大概率tab | 0.173s | 0.28/0.06 | A_cat=0 type1=0 csp=104 drpy=2 guard=0 豆瓣类=1 | `https://qist.wyfc.qzz.io/xiaosa/api.json` |
| 11 | my_124 | B-大概率tab | 0.503s | 0.51/0.49 | A_cat=0 type1=0 csp=1 drpy=1 guard=0 豆瓣类=0 | `http://124.223.214.31:8/api.json` |
| 12 | 摸鱼儿_fish | B-大概率tab | 0.627s | 0.74/0.51 | A_cat=0 type1=0 csp=99 drpy=0 guard=0 豆瓣类=0 | `https://6800.kstore.vip/fish.json` |
| 13 | 软件_47 | B-大概率tab | 0.766s | 0.77/0.76 | A_cat=0 type1=0 csp=76 drpy=13 guard=0 豆瓣类=1 | `http://47.96.82.41:5188/api.json` |
| 14 | xn6 | B-大概率tab | 1.528s | 1.52/1.54 | A_cat=0 type1=0 csp=45 drpy=1 guard=0 豆瓣类=1 | `http://xn--6orr3pi6g9uu.top/` |
| 15 | 俊哥_jundie | B-大概率tab | 1.732s | 1.37/2.09 | A_cat=0 type1=0 csp=22 drpy=2 guard=0 豆瓣类=0 | `http://home.jundie.top:81/top98.json` |
| 16 | 1_vip | B-大概率tab | 1.843s | 2.03/1.65 | A_cat=0 type1=0 csp=36 drpy=0 guard=0 豆瓣类=1 | `https://700sjro44343.vicp.fun/vip/vip/tv.json` |
| 17 | 二月红_0211 | B-大概率tab | 1.848s | 1.94/1.76 | A_cat=0 type1=0 csp=36 drpy=0 guard=0 豆瓣类=1 | `https://700sjro44343.vicp.fun/eggp/0211/tv.json` |
| 18 | 牛二 | C-存疑 | 0.593s | 0.38/0.81 | A_cat=0 type1=0 csp=0 drpy=0 guard=99 豆瓣类=0 | `https://9280.kstore.space/newwex.json` |
| 19 | 王二小 | C-存疑 | 0.696s | 0.60/0.80 | A_cat=0 type1=0 csp=0 drpy=0 guard=99 豆瓣类=0 | `https://9280.kstore.vip/newwex.json` |
| 20 | 牛儿 | C-存疑 | 0.740s | 0.70/0.78 | A_cat=0 type1=0 csp=0 drpy=0 guard=63 豆瓣类=0 | `https://9280.kstore.space/wex.json` |

## ❌ 无效/失败

| 接口名称 | 平均耗时 | HTTP | 原因 | URL |
|:-------:|:------:|:----:|------|-----|
| 小苹果_xpg | 0.071s | HTTP Error 404: Not Found/HTTP Error 404: Not Found | 空内容 | `https://bitbucket.org/xduo/duoapi/raw/master/xpg.json` |
| cs_nxog | 0.496s | HTTP Error 403: Forbidden/HTTP Error 403: Forbidden | 空内容 | `http://tv.nxog.top/m/` |
| fmys | 0.833s | HTTP Error 404: Not Found/HTTP Error 404: Not Found | 空内容 | `http://fmys.top/fmys.json` |
