# TVBox 订阅源分析报告（agent 内部参考，勿交付用户）

数据源: https://tvbox.wpcoder.cn/user.php

## ✅ 有效源（含 tab 分级）

| # | 名称 | tab级别 | 平均耗时 | 两次耗时 | 内容校验 | URL |
|:-:|------|:------:|:------:|:------:|---------|-----|
| 1 | 荐片_0821 | A-必有tab | 0.096s | 0.14/0.05 | A_cat=3 type1=2 csp=2 drpy=21 guard=0 豆瓣类=0 | `https://tv.203511.xyz/0821.json` |
| 2 | ok_liucn | A-必有tab | 0.142s | 0.23/0.05 | A_cat=11 type1=4 csp=164 drpy=54 guard=0 豆瓣类=1 | `https://raw.liucn.cc/box/m.json` |
| 3 | 11_liu673cn | A-必有tab | 0.172s | 0.27/0.08 | A_cat=11 type1=4 csp=164 drpy=54 guard=0 豆瓣类=1 | `https://cdn.jsdelivr.net/gh/liu673cn/box@main/m.json` |
| 4 | 小盒子4K | A-必有tab | 0.182s | 0.22/0.14 | A_cat=6 type1=3 csp=37 drpy=6 guard=0 豆瓣类=1 | `http://xhztv.top/4k.json` |
| 5 | 拾光_svip | A-必有tab | 0.183s | 0.21/0.15 | A_cat=24 type1=8 csp=135 drpy=77 guard=0 豆瓣类=1 | `https://gh-proxy.com/https://raw.githubusercontent.com/xmbjm/svip/refs/heads/main/svip.json` |
| 6 | 神秘大佬_jsm | A-必有tab | 0.192s | 0.29/0.09 | A_cat=8 type1=7 csp=108 drpy=34 guard=0 豆瓣类=0 | `https://g.33445500.xyz/https://raw.githubusercontent.com/qist/tvbox/refs/heads/master/jsm.json` |
| 7 | 1_vip | A-必有tab | 2.236s | 2.76/1.71 | A_cat=1 type1=0 csp=26 drpy=0 guard=0 豆瓣类=1 | `https://700sjro44343.vicp.fun/vip/vip/tv.json` |
| 8 | 金鹰_550 | A-必有tab | 2.584s | 4.15/1.01 | A_cat=14 type1=0 csp=79 drpy=7 guard=0 豆瓣类=1 | `http://550.3vcn.work/wdjyys.json` |
| 9 | 二月红_0211 | A-必有tab | 4.209s | 6.80/1.62 | A_cat=1 type1=0 csp=26 drpy=0 guard=0 豆瓣类=1 | `https://700sjro44343.vicp.fun/eggp/0211/tv.json` |
| 10 | 饭太硬_fty | B-大概率tab | 0.080s | 0.08/0.08 | A_cat=0 type1=0 csp=0 drpy=3 guard=45 豆瓣类=0 | `https://qist.wyfc.qzz.io/fty.json` |
| 11 | 潇洒_g334 | B-大概率tab | 0.122s | 0.16/0.09 | A_cat=0 type1=0 csp=108 drpy=2 guard=0 豆瓣类=1 | `https://g.33445500.xyz/https://raw.githubusercontent.com/qist/tvbox/refs/heads/master/xiaosa/api.json` |
| 12 | 潇洒_qist | B-大概率tab | 0.201s | 0.31/0.09 | A_cat=0 type1=0 csp=108 drpy=2 guard=0 豆瓣类=1 | `https://qist.wyfc.qzz.io/xiaosa/api.json` |
| 13 | 摸鱼儿_fish | B-大概率tab | 0.500s | 0.47/0.53 | A_cat=0 type1=0 csp=103 drpy=0 guard=0 豆瓣类=0 | `https://6800.kstore.vip/fish.json` |
| 14 | 软件_47 | B-大概率tab | 0.531s | 0.53/0.53 | A_cat=0 type1=0 csp=76 drpy=13 guard=0 豆瓣类=1 | `http://47.96.82.41:5188/api.json` |
| 15 | 俊哥_jundie | B-大概率tab | 0.999s | 1.11/0.89 | A_cat=0 type1=0 csp=22 drpy=2 guard=0 豆瓣类=0 | `http://home.jundie.top:81/top98.json` |
| 16 | my_124 | B-大概率tab | 1.093s | 1.79/0.39 | A_cat=0 type1=0 csp=1 drpy=1 guard=0 豆瓣类=0 | `http://124.223.214.31:8/api.json` |
| 17 | xn6 | B-大概率tab | 1.487s | 1.67/1.30 | A_cat=0 type1=0 csp=45 drpy=1 guard=0 豆瓣类=1 | `http://xn--6orr3pi6g9uu.top/` |
| 18 | 牛儿 | C-存疑 | 0.530s | 0.62/0.44 | A_cat=0 type1=0 csp=0 drpy=0 guard=63 豆瓣类=0 | `https://9280.kstore.space/wex.json` |
| 19 | 牛二 | C-存疑 | 0.567s | 0.54/0.60 | A_cat=0 type1=0 csp=0 drpy=0 guard=98 豆瓣类=0 | `https://9280.kstore.space/newwex.json` |
| 20 | 王二小 | C-存疑 | 0.682s | 0.91/0.45 | A_cat=0 type1=0 csp=0 drpy=0 guard=98 豆瓣类=0 | `https://9280.kstore.vip/newwex.json` |

## ❌ 无效/失败

| 接口名称 | 平均耗时 | HTTP | 原因 | URL |
|:-------:|:------:|:----:|------|-----|
| 小苹果_xpg | 0.137s | HTTP Error 404: Not Found/HTTP Error 404: Not Found | 空内容 | `https://bitbucket.org/xduo/duoapi/raw/master/xpg.json` |
| cs_nxog | 0.573s | HTTP Error 403: Forbidden/HTTP Error 403: Forbidden | 空内容 | `http://tv.nxog.top/m/` |
| fmys | 0.658s | HTTP Error 404: Not Found/HTTP Error 404: Not Found | 空内容 | `http://fmys.top/fmys.json` |
