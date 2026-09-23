# TVBox 订阅源分析报告（agent 内部参考，勿交付用户）

数据源: https://tvbox.wpcoder.cn/user.php

## ✅ 有效源（含 tab 分级）

| # | 名称 | tab级别 | 平均耗时 | 两次耗时 | 内容校验 | URL |
|:-:|------|:------:|:------:|:------:|---------|-----|
| 1 | 神秘大佬_jsm | A-必有tab | 0.109s | 0.13/0.09 | A_cat=8 type1=7 csp=104 drpy=32 guard=0 豆瓣类=0 | `https://g.33445500.xyz/https://raw.githubusercontent.com/qist/tvbox/refs/heads/master/jsm.json` |
| 2 | 拾光_svip | A-必有tab | 0.134s | 0.11/0.16 | A_cat=24 type1=8 csp=135 drpy=77 guard=0 豆瓣类=1 | `https://gh-proxy.com/https://raw.githubusercontent.com/xmbjm/svip/refs/heads/main/svip.json` |
| 3 | 荐片_0821 | A-必有tab | 0.143s | 0.19/0.09 | A_cat=3 type1=2 csp=2 drpy=21 guard=0 豆瓣类=0 | `https://tv.203511.xyz/0821.json` |
| 4 | ok_liucn | A-必有tab | 0.160s | 0.22/0.10 | A_cat=11 type1=4 csp=164 drpy=54 guard=0 豆瓣类=1 | `https://raw.liucn.cc/box/m.json` |
| 5 | 小盒子4K | A-必有tab | 0.190s | 0.13/0.25 | A_cat=6 type1=3 csp=37 drpy=6 guard=0 豆瓣类=1 | `http://xhztv.top/4k.json` |
| 6 | 11_liu673cn | A-必有tab | 0.196s | 0.35/0.04 | A_cat=11 type1=4 csp=164 drpy=54 guard=0 豆瓣类=1 | `https://cdn.jsdelivr.net/gh/liu673cn/box@main/m.json` |
| 7 | 金鹰_550 | A-必有tab | 2.334s | 3.38/1.29 | A_cat=14 type1=0 csp=79 drpy=7 guard=0 豆瓣类=1 | `http://550.3vcn.work/wdjyys.json` |
| 8 | 饭太硬_fty | B-大概率tab | 0.116s | 0.13/0.10 | A_cat=0 type1=0 csp=0 drpy=3 guard=44 豆瓣类=0 | `https://qist.wyfc.qzz.io/fty.json` |
| 9 | 潇洒_qist | B-大概率tab | 0.147s | 0.15/0.14 | A_cat=0 type1=0 csp=104 drpy=0 guard=0 豆瓣类=1 | `https://qist.wyfc.qzz.io/xiaosa/api.json` |
| 10 | 潇洒_g334 | B-大概率tab | 0.186s | 0.19/0.18 | A_cat=0 type1=0 csp=104 drpy=0 guard=0 豆瓣类=1 | `https://g.33445500.xyz/https://raw.githubusercontent.com/qist/tvbox/refs/heads/master/xiaosa/api.json` |
| 11 | 软件_47 | B-大概率tab | 0.668s | 0.67/0.66 | A_cat=0 type1=0 csp=76 drpy=13 guard=0 豆瓣类=1 | `http://47.96.82.41:5188/api.json` |
| 12 | my_124 | B-大概率tab | 0.801s | 0.83/0.77 | A_cat=0 type1=0 csp=109 drpy=7 guard=0 豆瓣类=1 | `http://124.223.214.31:8/api.json` |
| 13 | 俊哥_jundie | B-大概率tab | 0.985s | 1.05/0.93 | A_cat=0 type1=0 csp=22 drpy=2 guard=0 豆瓣类=0 | `http://home.jundie.top:81/top98.json` |
| 14 | 1_vip | B-大概率tab | 1.636s | 1.61/1.66 | A_cat=0 type1=0 csp=40 drpy=0 guard=0 豆瓣类=1 | `https://700sjro44343.vicp.fun/vip/vip/tv.json` |
| 15 | 二月红_0211 | B-大概率tab | 1.638s | 1.65/1.62 | A_cat=0 type1=0 csp=40 drpy=0 guard=0 豆瓣类=1 | `https://700sjro44343.vicp.fun/eggp/0211/tv.json` |
| 16 | 王二小 | C-存疑 | 0.377s | 0.53/0.22 | A_cat=0 type1=0 csp=0 drpy=0 guard=96 豆瓣类=0 | `https://9280.kstore.vip/newwex.json` |
| 17 | 牛儿 | C-存疑 | 0.511s | 0.55/0.47 | A_cat=0 type1=0 csp=0 drpy=0 guard=63 豆瓣类=0 | `https://9280.kstore.space/wex.json` |
| 18 | 牛二 | C-存疑 | 0.520s | 0.53/0.51 | A_cat=0 type1=0 csp=0 drpy=0 guard=96 豆瓣类=0 | `https://9280.kstore.space/newwex.json` |

## ❌ 无效/失败

| 接口名称 | 平均耗时 | HTTP | 原因 | URL |
|:-------:|:------:|:----:|------|-----|
| 小苹果_xpg | 0.188s | HTTP Error 404: Not Found/HTTP Error 404: Not Found | 空内容 | `https://bitbucket.org/xduo/duoapi/raw/master/xpg.json` |
| 摸鱼儿_fish | 0.458s | HTTP Error 401: /HTTP Error 401:  | 空内容 | `https://6800.kstore.vip/fish.json` |
| cs_nxog | 0.560s | HTTP Error 403: Forbidden/HTTP Error 403: Forbidden | 空内容 | `http://tv.nxog.top/m/` |
| fmys | 0.784s | HTTP Error 404: Not Found/HTTP Error 404: Not Found | 空内容 | `http://fmys.top/fmys.json` |
| xn6 | 5.631s | 200/HTTP Error 504: Gateway Time-out | sites=50个(有效api:50) | `http://xn--6orr3pi6g9uu.top/` |
