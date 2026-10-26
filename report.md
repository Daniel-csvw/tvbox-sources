# TVBox 订阅源分析报告（agent 内部参考，勿交付用户）

数据源: https://tvbox.wpcoder.cn/user.php

## ✅ 有效源（含 tab 分级）

| # | 名称 | tab级别 | 平均耗时 | 两次耗时 | 内容校验 | URL |
|:-:|------|:------:|:------:|:------:|---------|-----|
| 1 | 11_liu673cn | A-必有tab | 0.055s | 0.07/0.05 | A_cat=11 type1=4 csp=164 drpy=54 guard=0 豆瓣类=1 | `https://cdn.jsdelivr.net/gh/liu673cn/box@main/m.json` |
| 2 | 荐片_0821 | A-必有tab | 0.089s | 0.11/0.07 | A_cat=3 type1=2 csp=2 drpy=21 guard=0 豆瓣类=0 | `https://tv.203511.xyz/0821.json` |
| 3 | 小盒子4K | A-必有tab | 0.092s | 0.09/0.09 | A_cat=6 type1=3 csp=37 drpy=6 guard=0 豆瓣类=1 | `http://xhztv.top/4k.json` |
| 4 | 拾光_svip | A-必有tab | 0.142s | 0.17/0.11 | A_cat=24 type1=8 csp=135 drpy=77 guard=0 豆瓣类=1 | `https://gh-proxy.com/https://raw.githubusercontent.com/xmbjm/svip/refs/heads/main/svip.json` |
| 5 | 神秘大佬_jsm | A-必有tab | 0.169s | 0.18/0.15 | A_cat=8 type1=7 csp=103 drpy=34 guard=0 豆瓣类=0 | `https://g.33445500.xyz/https://raw.githubusercontent.com/qist/tvbox/refs/heads/master/jsm.json` |
| 6 | ok_liucn | A-必有tab | 0.248s | 0.21/0.29 | A_cat=11 type1=4 csp=164 drpy=54 guard=0 豆瓣类=1 | `https://raw.liucn.cc/box/m.json` |
| 7 | xn6 | A-必有tab | 1.041s | 1.30/0.78 | A_cat=0 type1=1 csp=45 drpy=2 guard=0 豆瓣类=1 | `http://xn--6orr3pi6g9uu.top/` |
| 8 | 金鹰_550 | A-必有tab | 1.340s | 1.69/0.99 | A_cat=14 type1=0 csp=79 drpy=7 guard=0 豆瓣类=1 | `http://550.3vcn.work/wdjyys.json` |
| 9 | 潇洒_g334 | B-大概率tab | 0.087s | 0.09/0.09 | A_cat=0 type1=0 csp=103 drpy=2 guard=0 豆瓣类=1 | `https://g.33445500.xyz/https://raw.githubusercontent.com/qist/tvbox/refs/heads/master/xiaosa/api.json` |
| 10 | 饭太硬_fty | B-大概率tab | 0.093s | 0.10/0.09 | A_cat=0 type1=0 csp=0 drpy=3 guard=46 豆瓣类=0 | `https://qist.wyfc.qzz.io/fty.json` |
| 11 | 潇洒_qist | B-大概率tab | 0.160s | 0.23/0.08 | A_cat=0 type1=0 csp=103 drpy=2 guard=0 豆瓣类=1 | `https://qist.wyfc.qzz.io/xiaosa/api.json` |
| 12 | 摸鱼儿_fish | B-大概率tab | 0.306s | 0.33/0.28 | A_cat=0 type1=0 csp=99 drpy=0 guard=0 豆瓣类=0 | `https://6800.kstore.vip/fish.json` |
| 13 | my_124 | B-大概率tab | 0.411s | 0.39/0.43 | A_cat=0 type1=0 csp=1 drpy=1 guard=0 豆瓣类=0 | `http://124.223.214.31:8/api.json` |
| 14 | 软件_47 | B-大概率tab | 0.626s | 0.64/0.61 | A_cat=0 type1=0 csp=76 drpy=13 guard=0 豆瓣类=1 | `http://47.96.82.41:5188/api.json` |
| 15 | 俊哥_jundie | B-大概率tab | 0.799s | 0.92/0.68 | A_cat=0 type1=0 csp=22 drpy=2 guard=0 豆瓣类=0 | `http://home.jundie.top:81/top98.json` |
| 16 | 二月红_0211 | B-大概率tab | 1.710s | 1.77/1.65 | A_cat=0 type1=0 csp=35 drpy=0 guard=0 豆瓣类=1 | `https://700sjro44343.vicp.fun/eggp/0211/tv.json` |
| 17 | 1_vip | B-大概率tab | 2.245s | 1.77/2.73 | A_cat=0 type1=0 csp=37 drpy=0 guard=0 豆瓣类=1 | `https://700sjro44343.vicp.fun/vip/vip/tv.json` |
| 18 | 王二小 | C-存疑 | 0.357s | 0.42/0.29 | A_cat=0 type1=0 csp=0 drpy=0 guard=99 豆瓣类=0 | `https://9280.kstore.vip/newwex.json` |
| 19 | 牛二 | C-存疑 | 0.357s | 0.27/0.44 | A_cat=0 type1=0 csp=0 drpy=0 guard=99 豆瓣类=0 | `https://9280.kstore.space/newwex.json` |
| 20 | 牛儿 | C-存疑 | 0.376s | 0.52/0.23 | A_cat=0 type1=0 csp=0 drpy=0 guard=63 豆瓣类=0 | `https://9280.kstore.space/wex.json` |

## ❌ 无效/失败

| 接口名称 | 平均耗时 | HTTP | 原因 | URL |
|:-------:|:------:|:----:|------|-----|
| 小苹果_xpg | 0.195s | HTTP Error 404: Not Found/HTTP Error 404: Not Found | 空内容 | `https://bitbucket.org/xduo/duoapi/raw/master/xpg.json` |
| cs_nxog | 0.409s | HTTP Error 403: Forbidden/HTTP Error 403: Forbidden | 空内容 | `http://tv.nxog.top/m/` |
| fmys | 0.588s | HTTP Error 404: Not Found/HTTP Error 404: Not Found | 空内容 | `http://fmys.top/fmys.json` |
