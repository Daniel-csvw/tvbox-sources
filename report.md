# TVBox 订阅源分析报告（agent 内部参考，勿交付用户）

数据源: https://tvbox.wpcoder.cn/user.php

## ✅ 有效源（含 tab 分级）

| # | 名称 | tab级别 | 平均耗时 | 两次耗时 | 内容校验 | URL |
|:-:|------|:------:|:------:|:------:|---------|-----|
| 1 | 小盒子4K | A-必有tab | 0.024s | 0.02/0.02 | A_cat=6 type1=3 csp=37 drpy=6 guard=0 豆瓣类=1 | `http://xhztv.top/4k.json` |
| 2 | ok_liucn | A-必有tab | 0.039s | 0.07/0.01 | A_cat=11 type1=4 csp=164 drpy=54 guard=0 豆瓣类=1 | `https://raw.liucn.cc/box/m.json` |
| 3 | 荐片_0821 | A-必有tab | 0.098s | 0.16/0.03 | A_cat=3 type1=2 csp=2 drpy=21 guard=0 豆瓣类=0 | `https://tv.203511.xyz/0821.json` |
| 4 | 神秘大佬_jsm | A-必有tab | 0.105s | 0.12/0.09 | A_cat=8 type1=7 csp=103 drpy=34 guard=0 豆瓣类=0 | `https://g.33445500.xyz/https://raw.githubusercontent.com/qist/tvbox/refs/heads/master/jsm.json` |
| 5 | 拾光_svip | A-必有tab | 0.144s | 0.20/0.08 | A_cat=24 type1=8 csp=135 drpy=77 guard=0 豆瓣类=1 | `https://gh-proxy.com/https://raw.githubusercontent.com/xmbjm/svip/refs/heads/main/svip.json` |
| 6 | 11_liu673cn | A-必有tab | 0.183s | 0.01/0.35 | A_cat=11 type1=4 csp=164 drpy=54 guard=0 豆瓣类=1 | `https://cdn.jsdelivr.net/gh/liu673cn/box@main/m.json` |
| 7 | xn6 | A-必有tab | 1.079s | 1.14/1.02 | A_cat=0 type1=1 csp=45 drpy=2 guard=0 豆瓣类=1 | `http://xn--6orr3pi6g9uu.top/` |
| 8 | 金鹰_550 | A-必有tab | 1.089s | 1.42/0.76 | A_cat=14 type1=0 csp=79 drpy=7 guard=0 豆瓣类=1 | `http://550.3vcn.work/wdjyys.json` |
| 9 | 饭太硬_fty | B-大概率tab | 0.070s | 0.08/0.06 | A_cat=0 type1=0 csp=0 drpy=3 guard=46 豆瓣类=0 | `https://qist.wyfc.qzz.io/fty.json` |
| 10 | 潇洒_g334 | B-大概率tab | 0.116s | 0.15/0.08 | A_cat=0 type1=0 csp=103 drpy=2 guard=0 豆瓣类=1 | `https://g.33445500.xyz/https://raw.githubusercontent.com/qist/tvbox/refs/heads/master/xiaosa/api.json` |
| 11 | 潇洒_qist | B-大概率tab | 0.139s | 0.19/0.09 | A_cat=0 type1=0 csp=103 drpy=2 guard=0 豆瓣类=1 | `https://qist.wyfc.qzz.io/xiaosa/api.json` |
| 12 | 摸鱼儿_fish | B-大概率tab | 0.330s | 0.52/0.14 | A_cat=0 type1=0 csp=104 drpy=0 guard=0 豆瓣类=0 | `https://6800.kstore.vip/fish.json` |
| 13 | my_124 | B-大概率tab | 0.418s | 0.43/0.40 | A_cat=0 type1=0 csp=1 drpy=1 guard=0 豆瓣类=0 | `http://124.223.214.31:8/api.json` |
| 14 | 软件_47 | B-大概率tab | 0.621s | 0.64/0.60 | A_cat=0 type1=0 csp=76 drpy=13 guard=0 豆瓣类=1 | `http://47.96.82.41:5188/api.json` |
| 15 | 二月红_0211 | B-大概率tab | 1.648s | 1.60/1.69 | A_cat=0 type1=0 csp=35 drpy=0 guard=0 豆瓣类=1 | `https://700sjro44343.vicp.fun/eggp/0211/tv.json` |
| 16 | 1_vip | B-大概率tab | 1.656s | 1.69/1.63 | A_cat=0 type1=0 csp=36 drpy=0 guard=0 豆瓣类=1 | `https://700sjro44343.vicp.fun/vip/vip/tv.json` |
| 17 | 牛二 | C-存疑 | 0.241s | 0.24/0.24 | A_cat=0 type1=0 csp=0 drpy=0 guard=99 豆瓣类=0 | `https://9280.kstore.space/newwex.json` |
| 18 | 王二小 | C-存疑 | 0.393s | 0.49/0.30 | A_cat=0 type1=0 csp=0 drpy=0 guard=99 豆瓣类=0 | `https://9280.kstore.vip/newwex.json` |
| 19 | 牛儿 | C-存疑 | 0.486s | 0.50/0.47 | A_cat=0 type1=0 csp=0 drpy=0 guard=63 豆瓣类=0 | `https://9280.kstore.space/wex.json` |

## ❌ 无效/失败

| 接口名称 | 平均耗时 | HTTP | 原因 | URL |
|:-------:|:------:|:----:|------|-----|
| 小苹果_xpg | 0.218s | HTTP Error 404: Not Found/HTTP Error 404: Not Found | 空内容 | `https://bitbucket.org/xduo/duoapi/raw/master/xpg.json` |
| cs_nxog | 0.361s | HTTP Error 403: Forbidden/HTTP Error 403: Forbidden | 空内容 | `http://tv.nxog.top/m/` |
| fmys | 0.552s | HTTP Error 404: Not Found/HTTP Error 404: Not Found | 空内容 | `http://fmys.top/fmys.json` |
| 俊哥_jundie | 12.213s | <urlopen error timed out>/<urlopen error timed out> | 空内容 | `http://home.jundie.top:81/top98.json` |
