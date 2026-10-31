# TVBox 订阅源分析报告（agent 内部参考，勿交付用户）

数据源: https://tvbox.wpcoder.cn/user.php

## ✅ 有效源（含 tab 分级）

| # | 名称 | tab级别 | 平均耗时 | 两次耗时 | 内容校验 | URL |
|:-:|------|:------:|:------:|:------:|---------|-----|
| 1 | 11_liu673cn | A-必有tab | 0.024s | 0.03/0.02 | A_cat=11 type1=4 csp=164 drpy=54 guard=0 豆瓣类=1 | `https://cdn.jsdelivr.net/gh/liu673cn/box@main/m.json` |
| 2 | 潇洒_g334 | A-必有tab | 0.087s | 0.08/0.09 | A_cat=0 type1=1 csp=105 drpy=2 guard=0 豆瓣类=1 | `https://g.33445500.xyz/https://raw.githubusercontent.com/qist/tvbox/refs/heads/master/xiaosa/api.json` |
| 3 | 荐片_0821 | A-必有tab | 0.094s | 0.14/0.05 | A_cat=3 type1=2 csp=2 drpy=21 guard=0 豆瓣类=0 | `https://tv.203511.xyz/0821.json` |
| 4 | 神秘大佬_jsm | A-必有tab | 0.107s | 0.15/0.07 | A_cat=8 type1=8 csp=105 drpy=34 guard=0 豆瓣类=0 | `https://g.33445500.xyz/https://raw.githubusercontent.com/qist/tvbox/refs/heads/master/jsm.json` |
| 5 | 拾光_svip | A-必有tab | 0.119s | 0.18/0.06 | A_cat=24 type1=8 csp=135 drpy=77 guard=0 豆瓣类=1 | `https://gh-proxy.com/https://raw.githubusercontent.com/xmbjm/svip/refs/heads/main/svip.json` |
| 6 | ok_liucn | A-必有tab | 0.147s | 0.28/0.01 | A_cat=11 type1=4 csp=164 drpy=54 guard=0 豆瓣类=1 | `https://raw.liucn.cc/box/m.json` |
| 7 | 潇洒_qist | A-必有tab | 0.157s | 0.26/0.06 | A_cat=0 type1=1 csp=105 drpy=2 guard=0 豆瓣类=1 | `https://qist.wyfc.qzz.io/xiaosa/api.json` |
| 8 | 小盒子4K | A-必有tab | 0.201s | 0.20/0.20 | A_cat=6 type1=3 csp=37 drpy=6 guard=0 豆瓣类=1 | `http://xhztv.top/4k.json` |
| 9 | 金鹰_550 | A-必有tab | 2.139s | 3.47/0.81 | A_cat=14 type1=0 csp=79 drpy=7 guard=0 豆瓣类=1 | `http://550.3vcn.work/wdjyys.json` |
| 10 | 二月红_0211 | A-必有tab | 2.714s | 2.57/2.86 | A_cat=1 type1=0 csp=26 drpy=0 guard=0 豆瓣类=1 | `https://700sjro44343.vicp.fun/eggp/0211/tv.json` |
| 11 | 1_vip | A-必有tab | 2.747s | 1.90/3.60 | A_cat=1 type1=0 csp=26 drpy=0 guard=0 豆瓣类=1 | `https://700sjro44343.vicp.fun/vip/vip/tv.json` |
| 12 | 饭太硬_fty | B-大概率tab | 0.066s | 0.08/0.06 | A_cat=0 type1=0 csp=0 drpy=3 guard=45 豆瓣类=0 | `https://qist.wyfc.qzz.io/fty.json` |
| 13 | my_124 | B-大概率tab | 0.488s | 0.48/0.49 | A_cat=0 type1=0 csp=1 drpy=1 guard=0 豆瓣类=0 | `http://124.223.214.31:8/api.json` |
| 14 | 摸鱼儿_fish | B-大概率tab | 0.661s | 0.75/0.57 | A_cat=0 type1=0 csp=102 drpy=0 guard=0 豆瓣类=0 | `https://6800.kstore.vip/fish.json` |
| 15 | 软件_47 | B-大概率tab | 0.697s | 0.69/0.70 | A_cat=0 type1=0 csp=76 drpy=13 guard=0 豆瓣类=1 | `http://47.96.82.41:5188/api.json` |
| 16 | 俊哥_jundie | B-大概率tab | 0.999s | 1.04/0.96 | A_cat=0 type1=0 csp=22 drpy=2 guard=0 豆瓣类=0 | `http://home.jundie.top:81/top98.json` |
| 17 | xn6 | B-大概率tab | 1.413s | 1.56/1.27 | A_cat=0 type1=0 csp=45 drpy=1 guard=0 豆瓣类=1 | `http://xn--6orr3pi6g9uu.top/` |
| 18 | 牛二 | C-存疑 | 0.491s | 0.39/0.59 | A_cat=0 type1=0 csp=0 drpy=0 guard=99 豆瓣类=0 | `https://9280.kstore.space/newwex.json` |
| 19 | 牛儿 | C-存疑 | 0.550s | 0.49/0.61 | A_cat=0 type1=0 csp=0 drpy=0 guard=63 豆瓣类=0 | `https://9280.kstore.space/wex.json` |
| 20 | 王二小 | C-存疑 | 0.598s | 0.78/0.41 | A_cat=0 type1=0 csp=0 drpy=0 guard=99 豆瓣类=0 | `https://9280.kstore.vip/newwex.json` |

## ❌ 无效/失败

| 接口名称 | 平均耗时 | HTTP | 原因 | URL |
|:-------:|:------:|:----:|------|-----|
| 小苹果_xpg | 0.251s | HTTP Error 404: Not Found/HTTP Error 404: Not Found | 空内容 | `https://bitbucket.org/xduo/duoapi/raw/master/xpg.json` |
| fmys | 0.911s | HTTP Error 404: Not Found/HTTP Error 404: Not Found | 空内容 | `http://fmys.top/fmys.json` |
| cs_nxog | 0.913s | HTTP Error 403: Forbidden/HTTP Error 403: Forbidden | 空内容 | `http://tv.nxog.top/m/` |
