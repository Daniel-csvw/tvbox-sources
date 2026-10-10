# TVBox 订阅源分析报告（agent 内部参考，勿交付用户）

数据源: https://tvbox.wpcoder.cn/user.php

## ✅ 有效源（含 tab 分级）

| # | 名称 | tab级别 | 平均耗时 | 两次耗时 | 内容校验 | URL |
|:-:|------|:------:|:------:|:------:|---------|-----|
| 1 | 荐片_0821 | A-必有tab | 0.154s | 0.23/0.08 | A_cat=3 type1=2 csp=2 drpy=21 guard=0 豆瓣类=0 | `https://tv.203511.xyz/0821.json` |
| 2 | 拾光_svip | A-必有tab | 0.163s | 0.19/0.14 | A_cat=24 type1=8 csp=135 drpy=77 guard=0 豆瓣类=1 | `https://gh-proxy.com/https://raw.githubusercontent.com/xmbjm/svip/refs/heads/main/svip.json` |
| 3 | 小盒子4K | A-必有tab | 0.175s | 0.21/0.14 | A_cat=6 type1=3 csp=37 drpy=6 guard=0 豆瓣类=1 | `http://xhztv.top/4k.json` |
| 4 | 11_liu673cn | A-必有tab | 0.200s | 0.08/0.32 | A_cat=11 type1=4 csp=164 drpy=54 guard=0 豆瓣类=1 | `https://cdn.jsdelivr.net/gh/liu673cn/box@main/m.json` |
| 5 | 神秘大佬_jsm | A-必有tab | 0.207s | 0.32/0.10 | A_cat=8 type1=7 csp=106 drpy=32 guard=0 豆瓣类=0 | `https://g.33445500.xyz/https://raw.githubusercontent.com/qist/tvbox/refs/heads/master/jsm.json` |
| 6 | ok_liucn | A-必有tab | 1.781s | 3.49/0.07 | A_cat=11 type1=4 csp=164 drpy=54 guard=0 豆瓣类=1 | `https://raw.liucn.cc/box/m.json` |
| 7 | 金鹰_550 | A-必有tab | 4.684s | 6.01/3.36 | A_cat=14 type1=0 csp=79 drpy=7 guard=0 豆瓣类=1 | `http://550.3vcn.work/wdjyys.json` |
| 8 | 饭太硬_fty | B-大概率tab | 0.088s | 0.08/0.09 | A_cat=0 type1=0 csp=0 drpy=3 guard=45 豆瓣类=0 | `https://qist.wyfc.qzz.io/fty.json` |
| 9 | 潇洒_g334 | B-大概率tab | 0.129s | 0.18/0.07 | A_cat=0 type1=0 csp=106 drpy=0 guard=0 豆瓣类=1 | `https://g.33445500.xyz/https://raw.githubusercontent.com/qist/tvbox/refs/heads/master/xiaosa/api.json` |
| 10 | my_124 | B-大概率tab | 0.445s | 0.45/0.44 | A_cat=0 type1=0 csp=1 drpy=1 guard=0 豆瓣类=0 | `http://124.223.214.31:8/api.json` |
| 11 | 软件_47 | B-大概率tab | 0.674s | 0.68/0.67 | A_cat=0 type1=0 csp=76 drpy=13 guard=0 豆瓣类=1 | `http://47.96.82.41:5188/api.json` |
| 12 | 俊哥_jundie | B-大概率tab | 0.993s | 1.00/0.99 | A_cat=0 type1=0 csp=22 drpy=2 guard=0 豆瓣类=0 | `http://home.jundie.top:81/top98.json` |
| 13 | 潇洒_qist | B-大概率tab | 1.238s | 2.39/0.09 | A_cat=0 type1=0 csp=106 drpy=0 guard=0 豆瓣类=1 | `https://qist.wyfc.qzz.io/xiaosa/api.json` |
| 14 | xn6 | B-大概率tab | 1.621s | 1.78/1.46 | A_cat=0 type1=0 csp=48 drpy=1 guard=0 豆瓣类=1 | `http://xn--6orr3pi6g9uu.top/` |
| 15 | 1_vip | B-大概率tab | 4.514s | 5.64/3.39 | A_cat=0 type1=0 csp=37 drpy=0 guard=0 豆瓣类=1 | `https://700sjro44343.vicp.fun/vip/vip/tv.json` |
| 16 | 二月红_0211 | B-大概率tab | 4.927s | 5.45/4.41 | A_cat=0 type1=0 csp=37 drpy=0 guard=0 豆瓣类=1 | `https://700sjro44343.vicp.fun/eggp/0211/tv.json` |
| 17 | 牛儿 | C-存疑 | 0.487s | 0.49/0.48 | A_cat=0 type1=0 csp=0 drpy=0 guard=63 豆瓣类=0 | `https://9280.kstore.space/wex.json` |
| 18 | 王二小 | C-存疑 | 0.487s | 0.49/0.48 | A_cat=0 type1=0 csp=0 drpy=0 guard=96 豆瓣类=0 | `https://9280.kstore.vip/newwex.json` |
| 19 | 牛二 | C-存疑 | 0.498s | 0.49/0.50 | A_cat=0 type1=0 csp=0 drpy=0 guard=96 豆瓣类=0 | `https://9280.kstore.space/newwex.json` |

## ❌ 无效/失败

| 接口名称 | 平均耗时 | HTTP | 原因 | URL |
|:-------:|:------:|:----:|------|-----|
| 小苹果_xpg | 0.134s | HTTP Error 404: Not Found/HTTP Error 404: Not Found | 空内容 | `https://bitbucket.org/xduo/duoapi/raw/master/xpg.json` |
| cs_nxog | 0.408s | HTTP Error 403: Forbidden/HTTP Error 403: Forbidden | 空内容 | `http://tv.nxog.top/m/` |
| 摸鱼儿_fish | 0.458s | HTTP Error 401: /HTTP Error 401:  | 空内容 | `https://6800.kstore.vip/fish.json` |
| fmys | 0.529s | HTTP Error 404: Not Found/HTTP Error 404: Not Found | 空内容 | `http://fmys.top/fmys.json` |
