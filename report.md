# TVBox 订阅源分析报告（agent 内部参考，勿交付用户）

数据源: https://tvbox.wpcoder.cn/user.php

## ✅ 有效源（含 tab 分级）

| # | 名称 | tab级别 | 平均耗时 | 两次耗时 | 内容校验 | URL |
|:-:|------|:------:|:------:|:------:|---------|-----|
| 1 | 11_liu673cn | A-必有tab | 0.024s | 0.03/0.02 | A_cat=11 type1=4 csp=164 drpy=54 guard=0 豆瓣类=1 | `https://cdn.jsdelivr.net/gh/liu673cn/box@main/m.json` |
| 2 | 荐片_0821 | A-必有tab | 0.097s | 0.13/0.06 | A_cat=3 type1=2 csp=2 drpy=21 guard=0 豆瓣类=0 | `https://tv.203511.xyz/0821.json` |
| 3 | 拾光_svip | A-必有tab | 0.122s | 0.19/0.06 | A_cat=24 type1=8 csp=135 drpy=77 guard=0 豆瓣类=1 | `https://gh-proxy.com/https://raw.githubusercontent.com/xmbjm/svip/refs/heads/main/svip.json` |
| 4 | 神秘大佬_jsm | A-必有tab | 0.170s | 0.27/0.07 | A_cat=8 type1=7 csp=106 drpy=32 guard=0 豆瓣类=0 | `https://g.33445500.xyz/https://raw.githubusercontent.com/qist/tvbox/refs/heads/master/jsm.json` |
| 5 | ok_liucn | A-必有tab | 0.178s | 0.35/0.01 | A_cat=11 type1=4 csp=164 drpy=54 guard=0 豆瓣类=1 | `https://raw.liucn.cc/box/m.json` |
| 6 | 小盒子4K | A-必有tab | 0.221s | 0.20/0.25 | A_cat=6 type1=3 csp=37 drpy=6 guard=0 豆瓣类=1 | `http://xhztv.top/4k.json` |
| 7 | 金鹰_550 | A-必有tab | 1.525s | 1.70/1.35 | A_cat=14 type1=0 csp=79 drpy=7 guard=0 豆瓣类=1 | `http://550.3vcn.work/wdjyys.json` |
| 8 | 饭太硬_fty | B-大概率tab | 0.072s | 0.07/0.08 | A_cat=0 type1=0 csp=0 drpy=3 guard=45 豆瓣类=0 | `https://qist.wyfc.qzz.io/fty.json` |
| 9 | 潇洒_g334 | B-大概率tab | 0.104s | 0.14/0.07 | A_cat=0 type1=0 csp=106 drpy=0 guard=0 豆瓣类=1 | `https://g.33445500.xyz/https://raw.githubusercontent.com/qist/tvbox/refs/heads/master/xiaosa/api.json` |
| 10 | 潇洒_qist | B-大概率tab | 0.272s | 0.49/0.05 | A_cat=0 type1=0 csp=106 drpy=0 guard=0 豆瓣类=1 | `https://qist.wyfc.qzz.io/xiaosa/api.json` |
| 11 | 软件_47 | B-大概率tab | 0.731s | 0.74/0.73 | A_cat=0 type1=0 csp=76 drpy=13 guard=0 豆瓣类=1 | `http://47.96.82.41:5188/api.json` |
| 12 | my_124 | B-大概率tab | 0.834s | 1.20/0.47 | A_cat=0 type1=0 csp=1 drpy=1 guard=0 豆瓣类=0 | `http://124.223.214.31:8/api.json` |
| 13 | 俊哥_jundie | B-大概率tab | 1.034s | 1.05/1.02 | A_cat=0 type1=0 csp=22 drpy=2 guard=0 豆瓣类=0 | `http://home.jundie.top:81/top98.json` |
| 14 | 二月红_0211 | B-大概率tab | 1.918s | 1.95/1.89 | A_cat=0 type1=0 csp=37 drpy=0 guard=0 豆瓣类=1 | `https://700sjro44343.vicp.fun/eggp/0211/tv.json` |
| 15 | 1_vip | B-大概率tab | 1.937s | 1.94/1.94 | A_cat=0 type1=0 csp=37 drpy=0 guard=0 豆瓣类=1 | `https://700sjro44343.vicp.fun/vip/vip/tv.json` |
| 16 | xn6 | B-大概率tab | 4.420s | 7.23/1.61 | A_cat=0 type1=0 csp=48 drpy=1 guard=0 豆瓣类=1 | `http://xn--6orr3pi6g9uu.top/` |
| 17 | 牛二 | C-存疑 | 0.405s | 0.44/0.37 | A_cat=0 type1=0 csp=0 drpy=0 guard=99 豆瓣类=0 | `https://9280.kstore.space/newwex.json` |
| 18 | 牛儿 | C-存疑 | 0.424s | 0.47/0.38 | A_cat=0 type1=0 csp=0 drpy=0 guard=63 豆瓣类=0 | `https://9280.kstore.space/wex.json` |
| 19 | 王二小 | C-存疑 | 0.799s | 0.59/1.01 | A_cat=0 type1=0 csp=0 drpy=0 guard=99 豆瓣类=0 | `https://9280.kstore.vip/newwex.json` |

## ❌ 无效/失败

| 接口名称 | 平均耗时 | HTTP | 原因 | URL |
|:-------:|:------:|:----:|------|-----|
| 小苹果_xpg | 0.171s | HTTP Error 404: Not Found/HTTP Error 404: Not Found | 空内容 | `https://bitbucket.org/xduo/duoapi/raw/master/xpg.json` |
| cs_nxog | 0.415s | HTTP Error 403: Forbidden/HTTP Error 403: Forbidden | 空内容 | `http://tv.nxog.top/m/` |
| 摸鱼儿_fish | 0.843s | HTTP Error 401: /HTTP Error 401:  | 空内容 | `https://6800.kstore.vip/fish.json` |
| fmys | 0.850s | HTTP Error 404: Not Found/HTTP Error 404: Not Found | 空内容 | `http://fmys.top/fmys.json` |
