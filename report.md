# TVBox 订阅源分析报告（agent 内部参考，勿交付用户）

数据源: https://tvbox.wpcoder.cn/user.php

## ✅ 有效源（含 tab 分级）

| # | 名称 | tab级别 | 平均耗时 | 两次耗时 | 内容校验 | URL |
|:-:|------|:------:|:------:|:------:|---------|-----|
| 1 | ok_liucn | A-必有tab | 0.120s | 0.21/0.03 | A_cat=11 type1=4 csp=164 drpy=54 guard=0 豆瓣类=1 | `https://raw.liucn.cc/box/m.json` |
| 2 | 荐片_0821 | A-必有tab | 0.128s | 0.20/0.06 | A_cat=3 type1=2 csp=2 drpy=21 guard=0 豆瓣类=0 | `https://tv.203511.xyz/0821.json` |
| 3 | 小盒子4K | A-必有tab | 0.135s | 0.14/0.13 | A_cat=6 type1=3 csp=37 drpy=6 guard=0 豆瓣类=1 | `http://xhztv.top/4k.json` |
| 4 | 神秘大佬_jsm | A-必有tab | 0.151s | 0.22/0.09 | A_cat=8 type1=7 csp=105 drpy=34 guard=0 豆瓣类=0 | `https://g.33445500.xyz/https://raw.githubusercontent.com/qist/tvbox/refs/heads/master/jsm.json` |
| 5 | 拾光_svip | A-必有tab | 0.155s | 0.24/0.07 | A_cat=24 type1=8 csp=135 drpy=77 guard=0 豆瓣类=1 | `https://gh-proxy.com/https://raw.githubusercontent.com/xmbjm/svip/refs/heads/main/svip.json` |
| 6 | 11_liu673cn | A-必有tab | 0.180s | 0.05/0.31 | A_cat=11 type1=4 csp=164 drpy=54 guard=0 豆瓣类=1 | `https://cdn.jsdelivr.net/gh/liu673cn/box@main/m.json` |
| 7 | 1_vip | A-必有tab | 1.367s | 1.22/1.51 | A_cat=1 type1=0 csp=27 drpy=0 guard=0 豆瓣类=1 | `https://700sjro44343.vicp.fun/vip/vip/tv.json` |
| 8 | 金鹰_550 | A-必有tab | 1.558s | 1.86/1.25 | A_cat=14 type1=0 csp=79 drpy=7 guard=0 豆瓣类=1 | `http://550.3vcn.work/wdjyys.json` |
| 9 | 二月红_0211 | A-必有tab | 2.187s | 1.82/2.55 | A_cat=1 type1=0 csp=26 drpy=0 guard=0 豆瓣类=1 | `https://700sjro44343.vicp.fun/eggp/0211/tv.json` |
| 10 | 饭太硬_fty | B-大概率tab | 0.096s | 0.07/0.12 | A_cat=0 type1=0 csp=0 drpy=3 guard=45 豆瓣类=0 | `https://qist.wyfc.qzz.io/fty.json` |
| 11 | 潇洒_g334 | B-大概率tab | 0.100s | 0.08/0.12 | A_cat=0 type1=0 csp=105 drpy=2 guard=0 豆瓣类=1 | `https://g.33445500.xyz/https://raw.githubusercontent.com/qist/tvbox/refs/heads/master/xiaosa/api.json` |
| 12 | 潇洒_qist | B-大概率tab | 0.128s | 0.20/0.06 | A_cat=0 type1=0 csp=105 drpy=2 guard=0 豆瓣类=1 | `https://qist.wyfc.qzz.io/xiaosa/api.json` |
| 13 | my_124 | B-大概率tab | 0.391s | 0.41/0.38 | A_cat=0 type1=0 csp=1 drpy=1 guard=0 豆瓣类=0 | `http://124.223.214.31:8/api.json` |
| 14 | 摸鱼儿_fish | B-大概率tab | 0.538s | 0.70/0.38 | A_cat=0 type1=0 csp=102 drpy=0 guard=0 豆瓣类=0 | `https://6800.kstore.vip/fish.json` |
| 15 | 软件_47 | B-大概率tab | 0.566s | 0.57/0.57 | A_cat=0 type1=0 csp=76 drpy=13 guard=0 豆瓣类=1 | `http://47.96.82.41:5188/api.json` |
| 16 | xn6 | B-大概率tab | 1.185s | 1.35/1.02 | A_cat=0 type1=0 csp=45 drpy=1 guard=0 豆瓣类=1 | `http://xn--6orr3pi6g9uu.top/` |
| 17 | 王二小 | C-存疑 | 0.264s | 0.34/0.18 | A_cat=0 type1=0 csp=0 drpy=0 guard=99 豆瓣类=0 | `https://9280.kstore.vip/newwex.json` |
| 18 | 牛二 | C-存疑 | 0.302s | 0.36/0.24 | A_cat=0 type1=0 csp=0 drpy=0 guard=99 豆瓣类=0 | `https://9280.kstore.space/newwex.json` |
| 19 | 牛儿 | C-存疑 | 0.313s | 0.31/0.32 | A_cat=0 type1=0 csp=0 drpy=0 guard=63 豆瓣类=0 | `https://9280.kstore.space/wex.json` |

## ❌ 无效/失败

| 接口名称 | 平均耗时 | HTTP | 原因 | URL |
|:-------:|:------:|:----:|------|-----|
| 小苹果_xpg | 0.210s | HTTP Error 404: Not Found/HTTP Error 404: Not Found | 空内容 | `https://bitbucket.org/xduo/duoapi/raw/master/xpg.json` |
| fmys | 0.536s | HTTP Error 404: Not Found/HTTP Error 404: Not Found | 空内容 | `http://fmys.top/fmys.json` |
| cs_nxog | 0.567s | HTTP Error 403: Forbidden/HTTP Error 403: Forbidden | 空内容 | `http://tv.nxog.top/m/` |
| 俊哥_jundie | 6.756s | 200/<urlopen error timed out> | sites=24个(有效api:24) | `http://home.jundie.top:81/top98.json` |
