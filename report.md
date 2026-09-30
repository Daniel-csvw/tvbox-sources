# TVBox 订阅源分析报告（agent 内部参考，勿交付用户）

数据源: https://tvbox.wpcoder.cn/user.php

## ✅ 有效源（含 tab 分级）

| # | 名称 | tab级别 | 平均耗时 | 两次耗时 | 内容校验 | URL |
|:-:|------|:------:|:------:|:------:|---------|-----|
| 1 | 11_liu673cn | A-必有tab | 0.025s | 0.04/0.01 | A_cat=11 type1=4 csp=164 drpy=54 guard=0 豆瓣类=1 | `https://cdn.jsdelivr.net/gh/liu673cn/box@main/m.json` |
| 2 | 荐片_0821 | A-必有tab | 0.092s | 0.12/0.06 | A_cat=3 type1=2 csp=2 drpy=21 guard=0 豆瓣类=0 | `https://tv.203511.xyz/0821.json` |
| 3 | ok_liucn | A-必有tab | 0.107s | 0.20/0.01 | A_cat=11 type1=4 csp=164 drpy=54 guard=0 豆瓣类=1 | `https://raw.liucn.cc/box/m.json` |
| 4 | 拾光_svip | A-必有tab | 0.156s | 0.24/0.07 | A_cat=24 type1=8 csp=135 drpy=77 guard=0 豆瓣类=1 | `https://gh-proxy.com/https://raw.githubusercontent.com/xmbjm/svip/refs/heads/main/svip.json` |
| 5 | 神秘大佬_jsm | A-必有tab | 0.185s | 0.30/0.07 | A_cat=8 type1=7 csp=102 drpy=32 guard=0 豆瓣类=0 | `https://g.33445500.xyz/https://raw.githubusercontent.com/qist/tvbox/refs/heads/master/jsm.json` |
| 6 | 小盒子4K | A-必有tab | 0.200s | 0.20/0.20 | A_cat=6 type1=3 csp=37 drpy=6 guard=0 豆瓣类=1 | `http://xhztv.top/4k.json` |
| 7 | 金鹰_550 | A-必有tab | 0.894s | 1.29/0.50 | A_cat=14 type1=0 csp=79 drpy=7 guard=0 豆瓣类=1 | `http://550.3vcn.work/wdjyys.json` |
| 8 | 饭太硬_fty | B-大概率tab | 0.059s | 0.05/0.07 | A_cat=0 type1=0 csp=0 drpy=3 guard=44 豆瓣类=0 | `https://qist.wyfc.qzz.io/fty.json` |
| 9 | 潇洒_g334 | B-大概率tab | 0.099s | 0.13/0.07 | A_cat=0 type1=0 csp=102 drpy=0 guard=0 豆瓣类=1 | `https://g.33445500.xyz/https://raw.githubusercontent.com/qist/tvbox/refs/heads/master/xiaosa/api.json` |
| 10 | 潇洒_qist | B-大概率tab | 0.154s | 0.25/0.06 | A_cat=0 type1=0 csp=102 drpy=0 guard=0 豆瓣类=1 | `https://qist.wyfc.qzz.io/xiaosa/api.json` |
| 11 | 软件_47 | B-大概率tab | 1.467s | 2.11/0.82 | A_cat=0 type1=0 csp=76 drpy=13 guard=0 豆瓣类=1 | `http://47.96.82.41:5188/api.json` |
| 12 | 二月红_0211 | B-大概率tab | 1.918s | 1.86/1.98 | A_cat=0 type1=0 csp=41 drpy=0 guard=0 豆瓣类=1 | `https://700sjro44343.vicp.fun/eggp/0211/tv.json` |
| 13 | xn6 | B-大概率tab | 1.966s | 1.98/1.96 | A_cat=0 type1=0 csp=48 drpy=1 guard=0 豆瓣类=1 | `http://xn--6orr3pi6g9uu.top/` |
| 14 | 1_vip | B-大概率tab | 2.018s | 1.89/2.14 | A_cat=0 type1=0 csp=41 drpy=0 guard=0 豆瓣类=1 | `https://700sjro44343.vicp.fun/vip/vip/tv.json` |
| 15 | 俊哥_jundie | B-大概率tab | 2.208s | 3.07/1.35 | A_cat=0 type1=0 csp=22 drpy=2 guard=0 豆瓣类=0 | `http://home.jundie.top:81/top98.json` |
| 16 | my_124 | B-大概率tab | 3.675s | 2.75/4.60 | A_cat=0 type1=0 csp=1 drpy=1 guard=0 豆瓣类=0 | `http://124.223.214.31:8/api.json` |
| 17 | 牛二 | C-存疑 | 0.469s | 0.46/0.48 | A_cat=0 type1=0 csp=0 drpy=0 guard=96 豆瓣类=0 | `https://9280.kstore.space/newwex.json` |
| 18 | 牛儿 | C-存疑 | 0.530s | 0.64/0.42 | A_cat=0 type1=0 csp=0 drpy=0 guard=63 豆瓣类=0 | `https://9280.kstore.space/wex.json` |
| 19 | 王二小 | C-存疑 | 0.605s | 0.47/0.74 | A_cat=0 type1=0 csp=0 drpy=0 guard=96 豆瓣类=0 | `https://9280.kstore.vip/newwex.json` |

## ❌ 无效/失败

| 接口名称 | 平均耗时 | HTTP | 原因 | URL |
|:-------:|:------:|:----:|------|-----|
| 小苹果_xpg | 0.051s | HTTP Error 404: Not Found/HTTP Error 404: Not Found | 空内容 | `https://bitbucket.org/xduo/duoapi/raw/master/xpg.json` |
| 摸鱼儿_fish | 0.380s | HTTP Error 401: /HTTP Error 401:  | 空内容 | `https://6800.kstore.vip/fish.json` |
| cs_nxog | 0.480s | HTTP Error 403: Forbidden/HTTP Error 403: Forbidden | 空内容 | `http://tv.nxog.top/m/` |
| fmys | 0.673s | HTTP Error 404: Not Found/HTTP Error 404: Not Found | 空内容 | `http://fmys.top/fmys.json` |
