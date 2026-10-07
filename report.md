# TVBox 订阅源分析报告（agent 内部参考，勿交付用户）

数据源: https://tvbox.wpcoder.cn/user.php

## ✅ 有效源（含 tab 分级）

| # | 名称 | tab级别 | 平均耗时 | 两次耗时 | 内容校验 | URL |
|:-:|------|:------:|:------:|:------:|---------|-----|
| 1 | 小盒子4K | A-必有tab | 0.018s | 0.02/0.01 | A_cat=6 type1=3 csp=37 drpy=6 guard=0 豆瓣类=1 | `http://xhztv.top/4k.json` |
| 2 | 11_liu673cn | A-必有tab | 0.021s | 0.02/0.02 | A_cat=11 type1=4 csp=164 drpy=54 guard=0 豆瓣类=1 | `https://cdn.jsdelivr.net/gh/liu673cn/box@main/m.json` |
| 3 | 荐片_0821 | A-必有tab | 0.049s | 0.05/0.05 | A_cat=3 type1=2 csp=2 drpy=21 guard=0 豆瓣类=0 | `https://tv.203511.xyz/0821.json` |
| 4 | 神秘大佬_jsm | A-必有tab | 0.075s | 0.08/0.07 | A_cat=8 type1=7 csp=102 drpy=32 guard=0 豆瓣类=0 | `https://g.33445500.xyz/https://raw.githubusercontent.com/qist/tvbox/refs/heads/master/jsm.json` |
| 5 | ok_liucn | A-必有tab | 0.081s | 0.15/0.01 | A_cat=11 type1=4 csp=164 drpy=54 guard=0 豆瓣类=1 | `https://raw.liucn.cc/box/m.json` |
| 6 | 拾光_svip | A-必有tab | 0.088s | 0.10/0.07 | A_cat=24 type1=8 csp=135 drpy=77 guard=0 豆瓣类=1 | `https://gh-proxy.com/https://raw.githubusercontent.com/xmbjm/svip/refs/heads/main/svip.json` |
| 7 | 金鹰_550 | A-必有tab | 4.752s | 7.60/1.91 | A_cat=14 type1=0 csp=79 drpy=7 guard=0 豆瓣类=1 | `http://550.3vcn.work/wdjyys.json` |
| 8 | 潇洒_g334 | B-大概率tab | 0.060s | 0.07/0.05 | A_cat=0 type1=0 csp=102 drpy=0 guard=0 豆瓣类=1 | `https://g.33445500.xyz/https://raw.githubusercontent.com/qist/tvbox/refs/heads/master/xiaosa/api.json` |
| 9 | 饭太硬_fty | B-大概率tab | 0.077s | 0.10/0.06 | A_cat=0 type1=0 csp=0 drpy=3 guard=45 豆瓣类=0 | `https://qist.wyfc.qzz.io/fty.json` |
| 10 | 潇洒_qist | B-大概率tab | 0.099s | 0.14/0.06 | A_cat=0 type1=0 csp=102 drpy=0 guard=0 豆瓣类=1 | `https://qist.wyfc.qzz.io/xiaosa/api.json` |
| 11 | my_124 | B-大概率tab | 0.414s | 0.39/0.44 | A_cat=0 type1=0 csp=1 drpy=1 guard=0 豆瓣类=0 | `http://124.223.214.31:8/api.json` |
| 12 | 软件_47 | B-大概率tab | 0.611s | 0.60/0.62 | A_cat=0 type1=0 csp=76 drpy=13 guard=0 豆瓣类=1 | `http://47.96.82.41:5188/api.json` |
| 13 | 俊哥_jundie | B-大概率tab | 0.878s | 1.11/0.65 | A_cat=0 type1=0 csp=22 drpy=2 guard=0 豆瓣类=0 | `http://home.jundie.top:81/top98.json` |
| 14 | xn6 | B-大概率tab | 1.259s | 1.30/1.21 | A_cat=0 type1=0 csp=48 drpy=1 guard=0 豆瓣类=1 | `http://xn--6orr3pi6g9uu.top/` |
| 15 | 1_vip | B-大概率tab | 1.513s | 1.65/1.38 | A_cat=0 type1=0 csp=37 drpy=0 guard=0 豆瓣类=1 | `https://700sjro44343.vicp.fun/vip/vip/tv.json` |
| 16 | 二月红_0211 | B-大概率tab | 1.878s | 1.64/2.11 | A_cat=0 type1=0 csp=37 drpy=0 guard=0 豆瓣类=1 | `https://700sjro44343.vicp.fun/eggp/0211/tv.json` |
| 17 | 牛二 | C-存疑 | 0.314s | 0.26/0.37 | A_cat=0 type1=0 csp=0 drpy=0 guard=96 豆瓣类=0 | `https://9280.kstore.space/newwex.json` |
| 18 | 牛儿 | C-存疑 | 0.388s | 0.62/0.16 | A_cat=0 type1=0 csp=0 drpy=0 guard=63 豆瓣类=0 | `https://9280.kstore.space/wex.json` |
| 19 | 王二小 | C-存疑 | 0.515s | 0.66/0.37 | A_cat=0 type1=0 csp=0 drpy=0 guard=96 豆瓣类=0 | `https://9280.kstore.vip/newwex.json` |

## ❌ 无效/失败

| 接口名称 | 平均耗时 | HTTP | 原因 | URL |
|:-------:|:------:|:----:|------|-----|
| 小苹果_xpg | 0.218s | HTTP Error 404: Not Found/HTTP Error 404: Not Found | 空内容 | `https://bitbucket.org/xduo/duoapi/raw/master/xpg.json` |
| cs_nxog | 0.311s | HTTP Error 403: Forbidden/HTTP Error 403: Forbidden | 空内容 | `http://tv.nxog.top/m/` |
| fmys | 0.576s | HTTP Error 404: Not Found/HTTP Error 404: Not Found | 空内容 | `http://fmys.top/fmys.json` |
| 摸鱼儿_fish | 0.604s | HTTP Error 401: /HTTP Error 401:  | 空内容 | `https://6800.kstore.vip/fish.json` |
