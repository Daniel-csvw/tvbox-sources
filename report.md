# TVBox 订阅源分析报告（agent 内部参考，勿交付用户）

数据源: https://tvbox.wpcoder.cn/user.php

## ✅ 有效源（含 tab 分级）

| # | 名称 | tab级别 | 平均耗时 | 两次耗时 | 内容校验 | URL |
|:-:|------|:------:|:------:|:------:|---------|-----|
| 1 | 11_liu673cn | A-必有tab | 0.027s | 0.03/0.02 | A_cat=11 type1=4 csp=164 drpy=54 guard=0 豆瓣类=1 | `https://cdn.jsdelivr.net/gh/liu673cn/box@main/m.json` |
| 2 | 神秘大佬_jsm | A-必有tab | 0.060s | 0.06/0.05 | A_cat=8 type1=8 csp=106 drpy=34 guard=0 豆瓣类=0 | `https://g.33445500.xyz/https://raw.githubusercontent.com/qist/tvbox/refs/heads/master/jsm.json` |
| 3 | ok_liucn | A-必有tab | 0.068s | 0.12/0.01 | A_cat=11 type1=4 csp=164 drpy=54 guard=0 豆瓣类=1 | `https://raw.liucn.cc/box/m.json` |
| 4 | 拾光_svip | A-必有tab | 0.092s | 0.10/0.08 | A_cat=24 type1=8 csp=135 drpy=77 guard=0 豆瓣类=1 | `https://gh-proxy.com/https://raw.githubusercontent.com/xmbjm/svip/refs/heads/main/svip.json` |
| 5 | 荐片_0821 | A-必有tab | 0.097s | 0.16/0.04 | A_cat=3 type1=2 csp=2 drpy=21 guard=0 豆瓣类=0 | `https://tv.203511.xyz/0821.json` |
| 6 | 小盒子4K | A-必有tab | 0.111s | 0.03/0.20 | A_cat=6 type1=3 csp=37 drpy=6 guard=0 豆瓣类=1 | `http://xhztv.top/4k.json` |
| 7 | 潇洒_g334 | A-必有tab | 0.120s | 0.17/0.07 | A_cat=0 type1=1 csp=106 drpy=2 guard=0 豆瓣类=1 | `https://g.33445500.xyz/https://raw.githubusercontent.com/qist/tvbox/refs/heads/master/xiaosa/api.json` |
| 8 | 潇洒_qist | A-必有tab | 0.151s | 0.25/0.05 | A_cat=0 type1=1 csp=106 drpy=2 guard=0 豆瓣类=1 | `https://qist.wyfc.qzz.io/xiaosa/api.json` |
| 9 | 金鹰_550 | A-必有tab | 0.948s | 1.19/0.71 | A_cat=14 type1=0 csp=79 drpy=7 guard=0 豆瓣类=1 | `http://550.3vcn.work/wdjyys.json` |
| 10 | 1_vip | A-必有tab | 1.833s | 2.51/1.16 | A_cat=1 type1=0 csp=26 drpy=0 guard=0 豆瓣类=1 | `https://700sjro44343.vicp.fun/vip/vip/tv.json` |
| 11 | 二月红_0211 | A-必有tab | 2.343s | 3.60/1.09 | A_cat=1 type1=0 csp=26 drpy=0 guard=0 豆瓣类=1 | `https://700sjro44343.vicp.fun/eggp/0211/tv.json` |
| 12 | 饭太硬_fty | B-大概率tab | 0.055s | 0.06/0.05 | A_cat=0 type1=0 csp=0 drpy=3 guard=45 豆瓣类=0 | `https://qist.wyfc.qzz.io/fty.json` |
| 13 | 摸鱼儿_fish | B-大概率tab | 0.247s | 0.24/0.26 | A_cat=0 type1=0 csp=103 drpy=0 guard=0 豆瓣类=0 | `https://6800.kstore.vip/fish.json` |
| 14 | my_124 | B-大概率tab | 0.419s | 0.42/0.42 | A_cat=0 type1=0 csp=1 drpy=1 guard=0 豆瓣类=0 | `http://124.223.214.31:8/api.json` |
| 15 | 软件_47 | B-大概率tab | 0.602s | 0.58/0.62 | A_cat=0 type1=0 csp=76 drpy=13 guard=0 豆瓣类=1 | `http://47.96.82.41:5188/api.json` |
| 16 | 俊哥_jundie | B-大概率tab | 0.964s | 0.89/1.04 | A_cat=0 type1=0 csp=22 drpy=2 guard=0 豆瓣类=0 | `http://home.jundie.top:81/top98.json` |
| 17 | xn6 | B-大概率tab | 0.965s | 1.07/0.86 | A_cat=0 type1=0 csp=45 drpy=1 guard=0 豆瓣类=1 | `http://xn--6orr3pi6g9uu.top/` |
| 18 | 王二小 | C-存疑 | 0.257s | 0.27/0.24 | A_cat=0 type1=0 csp=0 drpy=0 guard=99 豆瓣类=0 | `https://9280.kstore.vip/newwex.json` |
| 19 | 牛二 | C-存疑 | 0.264s | 0.29/0.24 | A_cat=0 type1=0 csp=0 drpy=0 guard=99 豆瓣类=0 | `https://9280.kstore.space/newwex.json` |
| 20 | 牛儿 | C-存疑 | 0.283s | 0.28/0.28 | A_cat=0 type1=0 csp=0 drpy=0 guard=63 豆瓣类=0 | `https://9280.kstore.space/wex.json` |

## ❌ 无效/失败

| 接口名称 | 平均耗时 | HTTP | 原因 | URL |
|:-------:|:------:|:----:|------|-----|
| 小苹果_xpg | 0.219s | HTTP Error 404: Not Found/HTTP Error 404: Not Found | 空内容 | `https://bitbucket.org/xduo/duoapi/raw/master/xpg.json` |
| cs_nxog | 0.503s | HTTP Error 403: Forbidden/HTTP Error 403: Forbidden | 空内容 | `http://tv.nxog.top/m/` |
| fmys | 0.570s | HTTP Error 404: Not Found/HTTP Error 404: Not Found | 空内容 | `http://fmys.top/fmys.json` |
