# TVBox 订阅源分析报告（agent 内部参考，勿交付用户）

数据源: https://tvbox.wpcoder.cn/user.php

## ✅ 有效源（含 tab 分级）

| # | 名称 | tab级别 | 平均耗时 | 两次耗时 | 内容校验 | URL |
|:-:|------|:------:|:------:|:------:|---------|-----|
| 1 | 11_liu673cn | A-必有tab | 0.064s | 0.11/0.02 | A_cat=11 type1=4 csp=164 drpy=54 guard=0 豆瓣类=1 | `https://cdn.jsdelivr.net/gh/liu673cn/box@main/m.json` |
| 2 | 拾光_svip | A-必有tab | 0.071s | 0.07/0.08 | A_cat=24 type1=8 csp=135 drpy=77 guard=0 豆瓣类=1 | `https://gh-proxy.com/https://raw.githubusercontent.com/xmbjm/svip/refs/heads/main/svip.json` |
| 3 | 荐片_0821 | A-必有tab | 0.074s | 0.10/0.05 | A_cat=3 type1=2 csp=2 drpy=21 guard=0 豆瓣类=0 | `https://tv.203511.xyz/0821.json` |
| 4 | ok_liucn | A-必有tab | 0.083s | 0.13/0.04 | A_cat=11 type1=4 csp=164 drpy=54 guard=0 豆瓣类=1 | `https://raw.liucn.cc/box/m.json` |
| 5 | 神秘大佬_jsm | A-必有tab | 0.137s | 0.18/0.10 | A_cat=8 type1=7 csp=104 drpy=32 guard=0 豆瓣类=0 | `https://g.33445500.xyz/https://raw.githubusercontent.com/qist/tvbox/refs/heads/master/jsm.json` |
| 6 | 小盒子4K | A-必有tab | 0.333s | 0.45/0.22 | A_cat=6 type1=3 csp=37 drpy=6 guard=0 豆瓣类=1 | `http://xhztv.top/4k.json` |
| 7 | 饭太硬_fty | B-大概率tab | 0.060s | 0.06/0.06 | A_cat=0 type1=0 csp=0 drpy=3 guard=46 豆瓣类=0 | `https://qist.wyfc.qzz.io/fty.json` |
| 8 | 潇洒_g334 | B-大概率tab | 0.095s | 0.13/0.06 | A_cat=0 type1=0 csp=104 drpy=0 guard=0 豆瓣类=1 | `https://g.33445500.xyz/https://raw.githubusercontent.com/qist/tvbox/refs/heads/master/xiaosa/api.json` |
| 9 | 潇洒_qist | B-大概率tab | 0.156s | 0.26/0.06 | A_cat=0 type1=0 csp=104 drpy=0 guard=0 豆瓣类=1 | `https://qist.wyfc.qzz.io/xiaosa/api.json` |
| 10 | 软件_47 | B-大概率tab | 0.748s | 0.76/0.73 | A_cat=0 type1=0 csp=76 drpy=13 guard=0 豆瓣类=1 | `http://47.96.82.41:5188/api.json` |
| 11 | my_124 | B-大概率tab | 0.840s | 1.16/0.52 | A_cat=0 type1=0 csp=1 drpy=1 guard=0 豆瓣类=0 | `http://124.223.214.31:8/api.json` |
| 12 | 俊哥_jundie | B-大概率tab | 1.079s | 1.05/1.11 | A_cat=0 type1=0 csp=22 drpy=2 guard=0 豆瓣类=0 | `http://home.jundie.top:81/top98.json` |
| 13 | xn6 | B-大概率tab | 1.610s | 1.73/1.49 | A_cat=0 type1=0 csp=48 drpy=1 guard=0 豆瓣类=1 | `http://xn--6orr3pi6g9uu.top/` |
| 14 | 二月红_0211 | B-大概率tab | 2.891s | 1.81/3.97 | A_cat=0 type1=0 csp=36 drpy=0 guard=0 豆瓣类=1 | `https://700sjro44343.vicp.fun/eggp/0211/tv.json` |
| 15 | 1_vip | B-大概率tab | 2.929s | 2.52/3.34 | A_cat=0 type1=0 csp=36 drpy=0 guard=0 豆瓣类=1 | `https://700sjro44343.vicp.fun/vip/vip/tv.json` |
| 16 | 牛儿 | C-存疑 | 0.668s | 0.73/0.60 | A_cat=0 type1=0 csp=0 drpy=0 guard=63 豆瓣类=0 | `https://9280.kstore.space/wex.json` |
| 17 | 王二小 | C-存疑 | 0.753s | 0.77/0.74 | A_cat=0 type1=0 csp=0 drpy=0 guard=99 豆瓣类=0 | `https://9280.kstore.vip/newwex.json` |
| 18 | 牛二 | C-存疑 | 0.793s | 0.83/0.76 | A_cat=0 type1=0 csp=0 drpy=0 guard=99 豆瓣类=0 | `https://9280.kstore.space/newwex.json` |

## ❌ 无效/失败

| 接口名称 | 平均耗时 | HTTP | 原因 | URL |
|:-------:|:------:|:----:|------|-----|
| 小苹果_xpg | 0.026s | HTTP Error 404: Not Found/HTTP Error 404: Not Found | 空内容 | `https://bitbucket.org/xduo/duoapi/raw/master/xpg.json` |
| cs_nxog | 0.470s | HTTP Error 403: Forbidden/HTTP Error 403: Forbidden | 空内容 | `http://tv.nxog.top/m/` |
| 摸鱼儿_fish | 0.799s | HTTP Error 401: /HTTP Error 401:  | 空内容 | `https://6800.kstore.vip/fish.json` |
| fmys | 0.817s | HTTP Error 404: Not Found/HTTP Error 404: Not Found | 空内容 | `http://fmys.top/fmys.json` |
| 金鹰_550 | 10.871s | timed out/200 | sites=106个(有效api:106) | `http://550.3vcn.work/wdjyys.json` |
