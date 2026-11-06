# TVBox 订阅源分析报告（agent 内部参考，勿交付用户）

数据源: https://tvbox.wpcoder.cn/user.php

## ✅ 有效源（含 tab 分级）

| # | 名称 | tab级别 | 平均耗时 | 两次耗时 | 内容校验 | URL |
|:-:|------|:------:|:------:|:------:|---------|-----|
| 1 | 11_liu673cn | A-必有tab | 0.065s | 0.11/0.02 | A_cat=11 type1=4 csp=164 drpy=54 guard=0 豆瓣类=1 | `https://cdn.jsdelivr.net/gh/liu673cn/box@main/m.json` |
| 2 | 荐片_0821 | A-必有tab | 0.089s | 0.11/0.07 | A_cat=3 type1=2 csp=2 drpy=21 guard=0 豆瓣类=0 | `https://tv.203511.xyz/0821.json` |
| 3 | 神秘大佬_jsm | A-必有tab | 0.105s | 0.12/0.09 | A_cat=8 type1=7 csp=108 drpy=34 guard=0 豆瓣类=0 | `https://g.33445500.xyz/https://raw.githubusercontent.com/qist/tvbox/refs/heads/master/jsm.json` |
| 4 | ok_liucn | A-必有tab | 0.108s | 0.19/0.02 | A_cat=11 type1=4 csp=164 drpy=54 guard=0 豆瓣类=1 | `https://raw.liucn.cc/box/m.json` |
| 5 | 拾光_svip | A-必有tab | 0.114s | 0.16/0.07 | A_cat=24 type1=8 csp=135 drpy=77 guard=0 豆瓣类=1 | `https://gh-proxy.com/https://raw.githubusercontent.com/xmbjm/svip/refs/heads/main/svip.json` |
| 6 | 小盒子4K | A-必有tab | 0.203s | 0.20/0.20 | A_cat=6 type1=3 csp=37 drpy=6 guard=0 豆瓣类=1 | `http://xhztv.top/4k.json` |
| 7 | 金鹰_550 | A-必有tab | 1.929s | 2.20/1.66 | A_cat=14 type1=0 csp=79 drpy=7 guard=0 豆瓣类=1 | `http://550.3vcn.work/wdjyys.json` |
| 8 | 二月红_0211 | A-必有tab | 1.934s | 1.95/1.92 | A_cat=1 type1=0 csp=26 drpy=0 guard=0 豆瓣类=1 | `https://700sjro44343.vicp.fun/eggp/0211/tv.json` |
| 9 | 1_vip | A-必有tab | 1.956s | 2.24/1.67 | A_cat=1 type1=0 csp=26 drpy=0 guard=0 豆瓣类=1 | `https://700sjro44343.vicp.fun/vip/vip/tv.json` |
| 10 | 饭太硬_fty | B-大概率tab | 0.067s | 0.06/0.07 | A_cat=0 type1=0 csp=0 drpy=3 guard=45 豆瓣类=0 | `https://qist.wyfc.qzz.io/fty.json` |
| 11 | 潇洒_qist | B-大概率tab | 0.114s | 0.16/0.07 | A_cat=0 type1=0 csp=108 drpy=2 guard=0 豆瓣类=1 | `https://qist.wyfc.qzz.io/xiaosa/api.json` |
| 12 | 潇洒_g334 | B-大概率tab | 0.121s | 0.15/0.10 | A_cat=0 type1=0 csp=108 drpy=2 guard=0 豆瓣类=1 | `https://g.33445500.xyz/https://raw.githubusercontent.com/qist/tvbox/refs/heads/master/xiaosa/api.json` |
| 13 | 摸鱼儿_fish | B-大概率tab | 0.631s | 0.70/0.56 | A_cat=0 type1=0 csp=104 drpy=0 guard=0 豆瓣类=0 | `https://6800.kstore.vip/fish.json` |
| 14 | 软件_47 | B-大概率tab | 0.763s | 0.77/0.76 | A_cat=0 type1=0 csp=76 drpy=13 guard=0 豆瓣类=1 | `http://47.96.82.41:5188/api.json` |
| 15 | my_124 | B-大概率tab | 1.019s | 0.49/1.55 | A_cat=0 type1=0 csp=1 drpy=1 guard=0 豆瓣类=0 | `http://124.223.214.31:8/api.json` |
| 16 | 俊哥_jundie | B-大概率tab | 1.079s | 1.08/1.08 | A_cat=0 type1=0 csp=22 drpy=2 guard=0 豆瓣类=0 | `http://home.jundie.top:81/top98.json` |
| 17 | xn6 | B-大概率tab | 1.426s | 1.64/1.21 | A_cat=0 type1=0 csp=43 drpy=1 guard=0 豆瓣类=1 | `http://xn--6orr3pi6g9uu.top/` |
| 18 | 牛二 | C-存疑 | 0.530s | 0.44/0.62 | A_cat=0 type1=0 csp=0 drpy=0 guard=100 豆瓣类=0 | `https://9280.kstore.space/newwex.json` |
| 19 | 牛儿 | C-存疑 | 0.533s | 0.58/0.49 | A_cat=0 type1=0 csp=0 drpy=0 guard=63 豆瓣类=0 | `https://9280.kstore.space/wex.json` |
| 20 | 王二小 | C-存疑 | 0.664s | 0.77/0.56 | A_cat=0 type1=0 csp=0 drpy=0 guard=100 豆瓣类=0 | `https://9280.kstore.vip/newwex.json` |

## ❌ 无效/失败

| 接口名称 | 平均耗时 | HTTP | 原因 | URL |
|:-------:|:------:|:----:|------|-----|
| 小苹果_xpg | 0.022s | HTTP Error 404: Not Found/HTTP Error 404: Not Found | 空内容 | `https://bitbucket.org/xduo/duoapi/raw/master/xpg.json` |
| fmys | 0.669s | HTTP Error 404: Not Found/HTTP Error 404: Not Found | 空内容 | `http://fmys.top/fmys.json` |
| cs_nxog | 0.858s | HTTP Error 403: Forbidden/HTTP Error 403: Forbidden | 空内容 | `http://tv.nxog.top/m/` |
