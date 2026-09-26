# TVBox 订阅源分析报告（agent 内部参考，勿交付用户）

数据源: https://tvbox.wpcoder.cn/user.php

## ✅ 有效源（含 tab 分级）

| # | 名称 | tab级别 | 平均耗时 | 两次耗时 | 内容校验 | URL |
|:-:|------|:------:|:------:|:------:|---------|-----|
| 1 | 11_liu673cn | A-必有tab | 0.121s | 0.14/0.10 | A_cat=11 type1=4 csp=164 drpy=54 guard=0 豆瓣类=1 | `https://cdn.jsdelivr.net/gh/liu673cn/box@main/m.json` |
| 2 | 荐片_0821 | A-必有tab | 0.133s | 0.20/0.07 | A_cat=3 type1=2 csp=2 drpy=21 guard=0 豆瓣类=0 | `https://tv.203511.xyz/0821.json` |
| 3 | ok_liucn | A-必有tab | 0.145s | 0.21/0.08 | A_cat=11 type1=4 csp=164 drpy=54 guard=0 豆瓣类=1 | `https://raw.liucn.cc/box/m.json` |
| 4 | 拾光_svip | A-必有tab | 0.181s | 0.21/0.16 | A_cat=24 type1=8 csp=135 drpy=77 guard=0 豆瓣类=1 | `https://gh-proxy.com/https://raw.githubusercontent.com/xmbjm/svip/refs/heads/main/svip.json` |
| 5 | 神秘大佬_jsm | A-必有tab | 0.254s | 0.40/0.11 | A_cat=8 type1=7 csp=103 drpy=32 guard=0 豆瓣类=0 | `https://g.33445500.xyz/https://raw.githubusercontent.com/qist/tvbox/refs/heads/master/jsm.json` |
| 6 | 小盒子4K | A-必有tab | 0.281s | 0.30/0.26 | A_cat=6 type1=3 csp=37 drpy=6 guard=0 豆瓣类=1 | `http://xhztv.top/4k.json` |
| 7 | 金鹰_550 | A-必有tab | 1.281s | 1.68/0.88 | A_cat=14 type1=0 csp=79 drpy=7 guard=0 豆瓣类=1 | `http://550.3vcn.work/wdjyys.json` |
| 8 | 饭太硬_fty | B-大概率tab | 0.102s | 0.10/0.11 | A_cat=0 type1=0 csp=0 drpy=3 guard=44 豆瓣类=0 | `https://qist.wyfc.qzz.io/fty.json` |
| 9 | 潇洒_g334 | B-大概率tab | 0.140s | 0.18/0.10 | A_cat=0 type1=0 csp=103 drpy=0 guard=0 豆瓣类=1 | `https://g.33445500.xyz/https://raw.githubusercontent.com/qist/tvbox/refs/heads/master/xiaosa/api.json` |
| 10 | 潇洒_qist | B-大概率tab | 0.201s | 0.31/0.09 | A_cat=0 type1=0 csp=103 drpy=0 guard=0 豆瓣类=1 | `https://qist.wyfc.qzz.io/xiaosa/api.json` |
| 11 | my_124 | B-大概率tab | 0.419s | 0.43/0.41 | A_cat=0 type1=0 csp=1 drpy=1 guard=0 豆瓣类=0 | `http://124.223.214.31:8/api.json` |
| 12 | 软件_47 | B-大概率tab | 0.666s | 0.69/0.64 | A_cat=0 type1=0 csp=76 drpy=13 guard=0 豆瓣类=1 | `http://47.96.82.41:5188/api.json` |
| 13 | 俊哥_jundie | B-大概率tab | 0.948s | 0.97/0.92 | A_cat=0 type1=0 csp=22 drpy=2 guard=0 豆瓣类=0 | `http://home.jundie.top:81/top98.json` |
| 14 | xn6 | B-大概率tab | 1.389s | 1.53/1.25 | A_cat=0 type1=0 csp=48 drpy=1 guard=0 豆瓣类=1 | `http://xn--6orr3pi6g9uu.top/` |
| 15 | 二月红_0211 | B-大概率tab | 1.651s | 1.69/1.61 | A_cat=0 type1=0 csp=39 drpy=0 guard=0 豆瓣类=1 | `https://700sjro44343.vicp.fun/eggp/0211/tv.json` |
| 16 | 1_vip | B-大概率tab | 1.700s | 1.83/1.57 | A_cat=0 type1=0 csp=39 drpy=0 guard=0 豆瓣类=1 | `https://700sjro44343.vicp.fun/vip/vip/tv.json` |
| 17 | 牛二 | C-存疑 | 0.398s | 0.40/0.40 | A_cat=0 type1=0 csp=0 drpy=0 guard=96 豆瓣类=0 | `https://9280.kstore.space/newwex.json` |
| 18 | 王二小 | C-存疑 | 0.447s | 0.54/0.36 | A_cat=0 type1=0 csp=0 drpy=0 guard=96 豆瓣类=0 | `https://9280.kstore.vip/newwex.json` |
| 19 | 牛儿 | C-存疑 | 0.465s | 0.55/0.38 | A_cat=0 type1=0 csp=0 drpy=0 guard=63 豆瓣类=0 | `https://9280.kstore.space/wex.json` |

## ❌ 无效/失败

| 接口名称 | 平均耗时 | HTTP | 原因 | URL |
|:-------:|:------:|:----:|------|-----|
| 小苹果_xpg | 0.149s | HTTP Error 404: Not Found/HTTP Error 404: Not Found | 空内容 | `https://bitbucket.org/xduo/duoapi/raw/master/xpg.json` |
| 摸鱼儿_fish | 0.425s | HTTP Error 401: /HTTP Error 401:  | 空内容 | `https://6800.kstore.vip/fish.json` |
| fmys | 0.538s | HTTP Error 404: Not Found/HTTP Error 404: Not Found | 空内容 | `http://fmys.top/fmys.json` |
| cs_nxog | 0.633s | HTTP Error 403: Forbidden/HTTP Error 403: Forbidden | 空内容 | `http://tv.nxog.top/m/` |
