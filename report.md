# TVBox 订阅源分析报告（agent 内部参考，勿交付用户）

数据源: https://tvbox.wpcoder.cn/user.php

## ✅ 有效源（含 tab 分级）

| # | 名称 | tab级别 | 平均耗时 | 两次耗时 | 内容校验 | URL |
|:-:|------|:------:|:------:|:------:|---------|-----|
| 1 | 11_liu673cn | A-必有tab | 0.032s | 0.04/0.03 | A_cat=11 type1=4 csp=164 drpy=54 guard=0 豆瓣类=1 | `https://cdn.jsdelivr.net/gh/liu673cn/box@main/m.json` |
| 2 | 神秘大佬_jsm | A-必有tab | 0.074s | 0.09/0.06 | A_cat=8 type1=7 csp=108 drpy=34 guard=0 豆瓣类=0 | `https://g.33445500.xyz/https://raw.githubusercontent.com/qist/tvbox/refs/heads/master/jsm.json` |
| 3 | 荐片_0821 | A-必有tab | 0.081s | 0.10/0.06 | A_cat=3 type1=2 csp=2 drpy=21 guard=0 豆瓣类=0 | `https://tv.203511.xyz/0821.json` |
| 4 | 小盒子4K | A-必有tab | 0.101s | 0.13/0.07 | A_cat=6 type1=3 csp=37 drpy=6 guard=0 豆瓣类=1 | `http://xhztv.top/4k.json` |
| 5 | ok_liucn | A-必有tab | 0.119s | 0.21/0.03 | A_cat=11 type1=4 csp=164 drpy=54 guard=0 豆瓣类=1 | `https://raw.liucn.cc/box/m.json` |
| 6 | 拾光_svip | A-必有tab | 0.127s | 0.15/0.10 | A_cat=24 type1=8 csp=135 drpy=77 guard=0 豆瓣类=1 | `https://gh-proxy.com/https://raw.githubusercontent.com/xmbjm/svip/refs/heads/main/svip.json` |
| 7 | 金鹰_550 | A-必有tab | 1.033s | 1.11/0.96 | A_cat=14 type1=0 csp=79 drpy=7 guard=0 豆瓣类=1 | `http://550.3vcn.work/wdjyys.json` |
| 8 | 1_vip | A-必有tab | 1.975s | 2.36/1.59 | A_cat=1 type1=0 csp=26 drpy=0 guard=0 豆瓣类=1 | `https://700sjro44343.vicp.fun/vip/vip/tv.json` |
| 9 | 二月红_0211 | A-必有tab | 2.070s | 3.14/1.00 | A_cat=1 type1=0 csp=26 drpy=0 guard=0 豆瓣类=1 | `https://700sjro44343.vicp.fun/eggp/0211/tv.json` |
| 10 | 潇洒_g334 | B-大概率tab | 0.057s | 0.06/0.06 | A_cat=0 type1=0 csp=108 drpy=2 guard=0 豆瓣类=1 | `https://g.33445500.xyz/https://raw.githubusercontent.com/qist/tvbox/refs/heads/master/xiaosa/api.json` |
| 11 | 饭太硬_fty | B-大概率tab | 0.069s | 0.07/0.07 | A_cat=0 type1=0 csp=0 drpy=3 guard=45 豆瓣类=0 | `https://qist.wyfc.qzz.io/fty.json` |
| 12 | 潇洒_qist | B-大概率tab | 0.115s | 0.15/0.08 | A_cat=0 type1=0 csp=108 drpy=2 guard=0 豆瓣类=1 | `https://qist.wyfc.qzz.io/xiaosa/api.json` |
| 13 | 摸鱼儿_fish | B-大概率tab | 0.393s | 0.40/0.39 | A_cat=0 type1=0 csp=104 drpy=0 guard=0 豆瓣类=0 | `https://6800.kstore.vip/fish.json` |
| 14 | 软件_47 | B-大概率tab | 0.581s | 0.60/0.56 | A_cat=0 type1=0 csp=76 drpy=13 guard=0 豆瓣类=1 | `http://47.96.82.41:5188/api.json` |
| 15 | 俊哥_jundie | B-大概率tab | 0.842s | 0.84/0.85 | A_cat=0 type1=0 csp=22 drpy=2 guard=0 豆瓣类=0 | `http://home.jundie.top:81/top98.json` |
| 16 | xn6 | B-大概率tab | 1.187s | 1.26/1.11 | A_cat=0 type1=0 csp=47 drpy=1 guard=0 豆瓣类=1 | `http://xn--6orr3pi6g9uu.top/` |
| 17 | my_124 | B-大概率tab | 1.266s | 1.00/1.53 | A_cat=0 type1=0 csp=1 drpy=1 guard=0 豆瓣类=0 | `http://124.223.214.31:8/api.json` |
| 18 | 牛儿 | C-存疑 | 0.294s | 0.41/0.18 | A_cat=0 type1=0 csp=0 drpy=0 guard=63 豆瓣类=0 | `https://9280.kstore.space/wex.json` |
| 19 | 王二小 | C-存疑 | 0.345s | 0.35/0.34 | A_cat=0 type1=0 csp=0 drpy=0 guard=100 豆瓣类=0 | `https://9280.kstore.vip/newwex.json` |
| 20 | 牛二 | C-存疑 | 0.350s | 0.33/0.37 | A_cat=0 type1=0 csp=0 drpy=0 guard=100 豆瓣类=0 | `https://9280.kstore.space/newwex.json` |

## ❌ 无效/失败

| 接口名称 | 平均耗时 | HTTP | 原因 | URL |
|:-------:|:------:|:----:|------|-----|
| 小苹果_xpg | 0.354s | HTTP Error 404: Not Found/HTTP Error 404: Not Found | 空内容 | `https://bitbucket.org/xduo/duoapi/raw/master/xpg.json` |
| fmys | 0.501s | HTTP Error 404: Not Found/HTTP Error 404: Not Found | 空内容 | `http://fmys.top/fmys.json` |
| cs_nxog | 0.570s | HTTP Error 403: Forbidden/HTTP Error 403: Forbidden | 空内容 | `http://tv.nxog.top/m/` |
