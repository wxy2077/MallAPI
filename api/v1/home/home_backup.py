#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/16 16:11
# @Author  : CoderCharm
# @File    : home_backup.py
# @Software: PyCharm
# @Desc    :
"""

备份数据直接查询sql

"""
from fastapi import APIRouter

router = APIRouter()


@router.get("/home/banner/backup", summary="路由中有backup的是相同路由备份信息")
async def home_banner():
    return {
        "code": 200,
        "msg": "success",
        "data": [
            {
                "link": "#",
                "image": "https://s11.mogucdn.com/mlcdn/c45406/200607_5k0d4fik4647258ajiegibb3keaij_1125x390.jpg"
            },
            {
                "link": "#",
                "image": "https://s11.mogucdn.com/mlcdn/c45406/200608_54l5j9i9gc3ikc09bhbkgdji1l3e1_1125x390.jpg"
            },
            {
                "link": "#",
                "image": "https://s5.mogucdn.com/mlcdn/c45406/200609_7kdh2e63b7a1i0d05c1f583hfhi07_1125x390.jpg"
            },
            {
                "link": "#",
                "image": "https://s11.mogucdn.com/mlcdn/c45406/200609_6784eldd3979cc9i9ife4233bah12_1125x390.jpg"
            },
            {
                "link": "#",
                "image": "https://s5.mogucdn.com/mlcdn/c45406/200609_21dakl66b60edja9k2hk02b5k21lc_1125x390.jpg"
            },
            {
                "link": "#",
                "image": "https://s10.mogucdn.com/mlcdn/c45406/180926_31eb9h75jc217k7iej24i2dd0jba3_750x390.jpg"
            },
            {
                "link": "#",
                "image": "https://s10.mogucdn.com/mlcdn/c45406/180926_45fkj8ifdj4l824l42dgf9hd0h495_750x390.jpg"
            },
            {
                "link": "#",
                "image": "https://s10.mogucdn.com/mlcdn/c45406/180926_31eb9h75jc217k7iej24i2dd0jba3_750x390.jpg"
            }
        ]
    }


@router.get("/home/features/backup", summary="首页轮播图下的四张图")
async def home_features():
    return {
        "code": 200,
        "msg": "success",
        "data": [
            {
                "link": "#",
                "image": "https://s10.mogucdn.com/mlcdn/c45406/180913_8d4e5adi8llg7c47lgh2291akiec7_225x225.png",
                "title": "初秋上新"
            },
            {
                "link": "#",
                "image": "https://s10.mogucdn.com/mlcdn/c45406/180913_387kgl3j21ff29lh04181iek48a6h_225x225.png",
                "title": "内购福利"
            },
            {
                "link": "#",
                "image": "https://s10.mogucdn.com/mlcdn/c45406/180913_25e804lk773hdk695c60cai492111_225x225.png",
                "title": "好物特卖"
            },
            {
                "link": "#",
                "image": "https://s10.mogucdn.com/mlcdn/c45406/180913_036dli57aah85cb82l1jj722g887g_225x225.png",
                "title": "十点抢卷"
            }
        ]
    }


@router.get("/home/recommends/backup", summary="首页推荐")
async def home_recommends():
    return {
        "code": 200,
        "msg": "success",
        "data": [
            {
                "cateId": 8,
                "cateName": "童装",
                "image": "https://s10.mogucdn.com/mlcdn/c45406/200327_0kllejc8c75ak5a942jd5f56ghh19_135x135.jpg_640x640.v1cAC.40.webp"
            },
            {
                "cateId": 7,
                "cateName": "男装",
                "image": "https://s10.mogucdn.com/mlcdn/c45406/200327_691e4fja6j2heh0egge060hfj7372_135x135.jpg_640x640.v1cAC.40.webp"
            },
            {
                "cateId": 6,
                "cateName": "家居",
                "image": "https://s10.mogucdn.com/mlcdn/c45406/200327_60hgbe9a54jd413df21l3gb468fa0_135x135.jpg_640x640.v1cAC.40.webp"
            },
            {
                "cateId": 5,
                "cateName": "套装",
                "image": "https://s10.mogucdn.com/mlcdn/c45406/200525_7lj1302k99cbh22ad37aild2c9b5a_135x135.jpg_640x640.v1cAC.40.webp"
            },
            {
                "cateId": 4,
                "cateName": "裙子",
                "image": "https://s10.mogucdn.com/mlcdn/c45406/200327_1a3d2egbb3cagj7cg9jk8k5e24ck2_135x135.jpg_640x640.v1cAC.40.webp"
            },
            {
                "cateId": 3,
                "cateName": "裤子",
                "image": "https://s10.mogucdn.com/mlcdn/c45406/191021_2cagf3kgj81d6895k8571g8jbj30e_135x135.jpg_640x640.v1cAC.40.webp"
            },
            {
                "cateId": 2,
                "cateName": "上衣",
                "image": "https://s10.mogucdn.com/mlcdn/c45406/190903_0572el03440fllf207k3g5kfe6g35_150x150.jpg_640x640.v1cAC.40.webp"
            },
            {
                "cateId": 1,
                "cateName": "女装",
                "image": "https://s10.mogucdn.com/mlcdn/c45406/200327_50ieadafgg13667jgf432hb2ijl9i_135x135.jpg_640x640.v1cAC.40.webp"
            }
        ]
    }


@router.get("/home/tab/backup", summary="首页推荐信息")
async def goods_tab():
    return {
        "code": 200,
        "msg": "success",
        "data": [
            {
                "tabId": 1001,
                "tabName": "流行"
            },
            {
                "tabId": 1002,
                "tabName": "精选"
            },
            {
                "tabId": 1003,
                "tabName": "新款"
            }
        ]
    }


@router.get("/home/goods/backup", summary="首页tab切换信息")
async def home_goods(tabId: int = 0, page: int = 1, pageSize: int = 10):
    return {
        "code": 200,
        "msg": "success",
        "data": [
            {
                "page": 1,
                "tabId": 1001,
                "tabName": "流行",
                "item": [
                    {
                        "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1lqmi5u&acm=3.mce.1_1_1lqmi5u.9750.44188-27059.cE47zs1uwNALZ.sd_115-swt_69-imt_7-c_2_11_331175047_0_7_0-lc_201-fcid_20003463-mid_9750-pit_30-c1_3_657254813_10000001-dit_169&cparam=MTU5MTc3MzgzNl8xZnU3eWg2XzgyNmNiMTJhMjJkNGViNmQzZjVjZmMxYTAxZDhhYWY4XzExXzZfMzMxMTc1MDQ3XzRkXzBfN18wXzY5M18xXzA=",
                        "image": "https://s5.mogucdn.com/mlcdn/c45406/190525_17e4877h3i4e1d8c9fb869g1kllle_640x960.jpg",
                        "title": "买1送牙刷抖音同款牙粉美牙膏口气清新去黄牙烟牙渍异味口腔护理",
                        "price": 39.9,
                        "collection": 7293
                    },
                    {
                        "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1mjjm7a&acm=3.mce.1_4_1mjjm7a.9750.36422.cE47ys1uwNAL0.sd_115-swt_69-imt_6-c_2_11_515577125_0_0_3-lc_201-fcid_20003463-mid_9750-pit_24-pm_003-dit_169&cparam=MTU5MTc3MzgzNl8xMWtfMzE1YTllYzllYTM1MTM1NGExYWMwODQ1OWU3MWZhOTRfMTFfMF81MTU1NzcxMjVfNGVfMF8wXzBfMTAwOF8xXzNfbG9jLTA=",
                        "image": "https://s5.mogucdn.com/mlcdn/c45406/190724_25hha590h023601484649g8fd654h_640x960.jpg",
                        "title": "春秋季新款韩版系带蝴蝶结收腰连衣裙女胖妹妹大码遮肚a字裙",
                        "price": 59,
                        "collection": 2951
                    },
                    {
                        "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1mgjqia&acm=3.mce.1_4_1mgjqia.9750.36422.cE47ys1uwNAL0.sd_115-swt_69-imt_6-c_2_11_501091676_0_0_3-lc_201-fcid_20003463-mid_9750-pit_24-pm_003-dit_169&cparam=MTU5MTc3MzgzNl8xMWtfMzE1YTllYzllYTM1MTM1NGExYWMwODQ1OWU3MWZhOTRfMTFfMF81MDEwOTE2NzZfNGNfMF8wXzBfODc0XzFfM19sb2MtMA==",
                        "image": "https://s5.mogucdn.com/mlcdn/c45406/190507_4c8876ei20ai58d713f421j1k75gg_800x1200.jpg",
                        "title": "韩版甜美小清新宽松显瘦雪纺衫防晒衫背心九分阔腿裤时尚套装夏季",
                        "price": 49,
                        "collection": 19060
                    },
                    {
                        "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1mgex20&acm=3.mce.1_4_1mgex20.9750.36422.cE47ys1uwNAL0.sd_115-swt_69-imt_6-c_2_11_501776339_0_0_3-lc_201-fcid_20003463-mid_9750-pit_24-pm_003-dit_169&cparam=MTU5MTc3MzgzNl8xMWtfMzE1YTllYzllYTM1MTM1NGExYWMwODQ1OWU3MWZhOTRfMTFfMF81MDE3NzYzMzlfNGVfMF8wXzBfMzkyXzFfM19sb2MtMA==",
                        "image": "https://s5.mogucdn.com/mlcdn/c45406/190503_4615igd6bh2afl511590k8gjadjee_750x1000.jpg",
                        "title": "牛仔老爹裤女高腰夏季新款宽松显瘦九分韩版百搭薄款小脚哈伦裤子",
                        "price": 69,
                        "collection": 9504
                    },
                    {
                        "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1mdlqpa&acm=3.mce.1_4_1mdlqpa.9750.36422.cE47ys1uwNAL0.sd_115-swt_69-imt_6-c_2_11_478270155_0_0_3-lc_201-fcid_20003463-mid_9750-pit_24-pm_003-dit_169&cparam=MTU5MTc3MzgzNl8xMWtfMzE1YTllYzllYTM1MTM1NGExYWMwODQ1OWU3MWZhOTRfMTFfMF80NzgyNzAxNTVfNGY4OV8wXzBfMF8xMjBfMV8zX2xvYy0w",
                        "image": "https://s5.mogucdn.com/mlcdn/c45406/190126_6iidc8k8996f24d79bk1d5blhgbl6_640x960.jpg",
                        "title": "chic上衣春秋季韩版胖妹妹宽松大码女装中长款长袖T恤女t学生原宿",
                        "price": 39.5,
                        "collection": 4046
                    },
                    {
                        "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1mhngau&acm=3.mce.1_4_1mhngau.9750.36422.cE47ys1uwNAL0.sd_115-swt_69-imt_6-c_2_11_505348322_0_0_3-lc_201-fcid_20003463-mid_9750-pit_24-pm_003-dit_169&cparam=MTU5MTc3MzgzNl8xMWtfMzE1YTllYzllYTM1MTM1NGExYWMwODQ1OWU3MWZhOTRfMTFfMF81MDUzNDgzMjJfNGNfMF8wXzBfODIzXzFfM19sb2MtMA==",
                        "image": "https://s5.mogucdn.com/mlcdn/c45406/190525_57bia657l5d572dd6kihdfgl4k53e_640x960.jpg",
                        "title": "夏季新款韩版气质女神范红色超仙娃娃领长裙收腰显瘦雪纺连衣裙女",
                        "price": 89,
                        "collection": 7851
                    },
                    {
                        "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1mjpbqs&acm=3.mce.1_4_1mjpbqs.9750.36422.cE47ys1uwNAL0.sd_115-swt_69-imt_6-c_2_11_516459591_0_0_3-lc_201-fcid_20003463-mid_9750-pit_24-pm_003-dit_169&cparam=MTU5MTc3MzgzNl8xMWtfMzE1YTllYzllYTM1MTM1NGExYWMwODQ1OWU3MWZhOTRfMTFfMF81MTY0NTk1OTFfNGY4ZF8wXzBfMF83ODhfMV8zX2xvYy0w",
                        "image": "https://s5.mogucdn.com/mlcdn/c45406/190730_0g98j14d2f6c4filadcl6bjl9gblk_640x850.jpg",
                        "title": "秋装女套装宽松格子衬衫+针织背心+ 高腰阔腿牛仔裤时尚三件套",
                        "price": 35,
                        "collection": 1802
                    },
                    {
                        "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1lp31fu&acm=3.mce.1_4_1lp31fu.9750.36422.cE47ys1uwNAL0.sd_115-swt_69-imt_6-c_2_11_403490188_0_0_3-lc_201-fcid_20003463-mid_9750-pit_24-pm_003-dit_169&cparam=MTU5MTc3MzgzNl8xMWtfMzE1YTllYzllYTM1MTM1NGExYWMwODQ1OWU3MWZhOTRfMTFfMF80MDM0OTAxODhfNGY4Zl8wXzBfMF8zNTBfMV8zX2xvYy0w",
                        "image": "https://s5.mogucdn.com/mlcdn/c45406/180102_75hcah3bk39k00215l5kb4h3af2f1_640x960.jpg",
                        "title": "新品韩版时尚大码气质女裤高腰纯色修身修长腿休闲裤大喇叭裤长裤",
                        "price": 69.3,
                        "collection": 1637
                    },
                    {
                        "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1mfxrbg&acm=3.mce.1_4_1mfxrbg.9750.36422.cE47ys1uwNAL0.sd_115-swt_69-imt_6-c_2_11_498571145_0_0_3-lc_201-fcid_20003463-mid_9750-pit_24-pm_003-dit_169&cparam=MTU5MTc3MzgzNl8xMWtfMzE1YTllYzllYTM1MTM1NGExYWMwODQ1OWU3MWZhOTRfMTFfMF80OTg1NzExNDVfNGNfMF8wXzBfMTgyXzFfM19sb2MtMA==",
                        "image": "https://s5.mogucdn.com/mlcdn/c45406/190427_5045eh4cagdi9fa13egb5ikf6c8id_640x959.jpg",
                        "title": "夏装女装2020新款韩版宽松不规则收腰短袖T恤女网红上衣服潮",
                        "price": 29.9,
                        "collection": 7928
                    },
                    {
                        "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1k9t008&acm=3.mce.1_1_1k9t008.9750.44188-27059.cE47zs1uwNALZ.sd_115-swt_69-imt_7-c_2_11_232294134_0_6_0-lc_201-fcid_20003463-mid_9750-pit_30-c1_3_612896520_10000001-dit_169&cparam=MTU5MTc3MzgzNl8xYXljZ25hX2JiNjY4MmFkMTcyZGQwMTA2MDk4OTg1ZjMxNWQ4ZjRhXzExXzVfMjMyMjk0MTM0XzRkXzBfNl8wXzI4NF8xXzA=",
                        "image": "https://s5.mogucdn.com/mlcdn/c45406/170501_3bdc7a3c58fgkfk2j1akl0iccejfg_640x960.jpg",
                        "title": "包邮 新款2019复古纯色小清新钱夹 学生时尚钱包女短款",
                        "price": 39.9,
                        "collection": 4623
                    }
                ]
            },
            {
                "page": 1,
                "tabId": 1002,
                "tabName": "精选",
                "item": [
                    {
                        "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1mkrm9i&acm=3.mce.1_1_1mkrm9i.9750.44188-27059.cE47zs1uWzM47.sd_115-swt_69-imt_7-c_2_11_556699730_0_24_0-lc_201-fcid_20003463-mid_9750-pit_30-c1_3_682568351_10000001-dit_149&cparam=MTU5MTc3OTk3OV8xMWtfN2M2YzAyZDY3MjgwNjZiZjRlY2ZlYzFkNDI0MThkZmJfMTFfN181NTY2OTk3MzBfNGRfMF8yNF8wXzQxMF8xXzA=",
                        "image": "https://s5.mogucdn.com/mlcdn/c45406/190906_59i021a4864jlg0731c462f516l3e_640x960.jpg",
                        "title": "儿童装男童春秋套装2020新款中大童男孩休闲运动两件套童装潮",
                        "price": 79.8,
                        "collection": 84
                    },
                    {
                        "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1ma3b0s&acm=3.mce.1_1_1ma3b0s.9750.44188-27059.cE47zs1uWzM47.sd_115-swt_69-imt_7-c_2_11_454684063_0_23_0-lc_201-fcid_20003463-mid_9750-pit_30-c1_3_673603114_10000001-dit_149&cparam=MTU5MTc3OTk3OV8xaWV3MGtjX2I5NTNhYjFjNjlhYjU3YjJkNzY4OTc1ZjZmZDJlYTVkXzExXzZfNDU0Njg0MDYzXzRkXzBfMjNfMF82OTRfMV8w",
                        "image": "https://s5.mogucdn.com/mlcdn/c45406/181019_055b79i095fg86ia2d0l51l3a0c5g_640x960.jpg",
                        "title": "2020夏季英伦男鞋子韩版潮流男鞋百搭休闲鞋男士椰子运动潮鞋",
                        "price": 159.9,
                        "collection": 862
                    },
                    {
                        "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1mq2ghy&acm=3.mce.1_4_1mq2ghy.9750.36422.cE47zs1uWzM48.sd_115-swt_69-imt_6-lc_201-fcid_20003463-mid_9750-pit_24-pm_003-dit_149",
                        "image": "https://s5.mogucdn.com/mlcdn/c45406/200118_7g1629744g4igl1jel60a63c0kc32_5999x8999.jpg",
                        "title": "米白色直筒女2020春季韩版初恋学生新款宽松复古休闲裤子",
                        "price": 39.9,
                        "collection": 154
                    },
                    {
                        "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1ml42jk&acm=3.mce.1_4_1ml42jk.9750.36422.cE47zs1uWzM48.sd_115-swt_69-imt_6-c_2_11_528424358_0_0_3-lc_201-fcid_20003463-mid_9750-pit_24-pm_003-dit_149&cparam=MTU5MTc3OTk3OV8xMWtfN2M2YzAyZDY3MjgwNjZiZjRlY2ZlYzFkNDI0MThkZmJfMTFfMF81Mjg0MjQzNThfNGM4Zl8wXzBfMF8xNDJfMV8zX2xvYy0w",
                        "image": "https://s5.mogucdn.com/mlcdn/c45406/190919_1577c5e3jfdgh074b0e6jg4bi4j72_3333x4999.jpg",
                        "title": "2020法式复古长袖连衣裙女春季新款小个子宽松收腰衬衫裙长裙",
                        "price": 99,
                        "collection": 4875
                    },
                    {
                        "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1m6m0bc&acm=3.mce.1_4_1m6m0bc.9750.36422.cE47zs1uWzM48.sd_115-swt_69-imt_6-c_2_11_421089381_0_0_3-lc_201-fcid_20003463-mid_9750-pit_24-pm_003-dit_149&cparam=MTU5MTc3OTk3OV8xMWtfN2M2YzAyZDY3MjgwNjZiZjRlY2ZlYzFkNDI0MThkZmJfMTFfMF80MjEwODkzODFfNGVfMF8wXzBfODA1XzFfM19sb2MtMA==",
                        "image": "https://s5.mogucdn.com/mlcdn/c45406/180729_00ga5gih02jefgh47248hk6h94bl4_640x960.jpg",
                        "title": "2020早春新款韩版宽松百搭中长款复古格子长袖衬衫外套上衣女",
                        "price": 59.5,
                        "collection": 5472
                    },
                    {
                        "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1mlkole&acm=3.mce.1_4_1mlkole.9750.36422.cE47zs1uWzM48.sd_115-swt_69-imt_6-c_2_11_536192861_0_0_3-lc_201-fcid_20003463-mid_9750-pit_24-pm_003-dit_149&cparam=MTU5MTc3OTk3OV8xMWtfN2M2YzAyZDY3MjgwNjZiZjRlY2ZlYzFkNDI0MThkZmJfMTFfMF81MzYxOTI4NjFfNGNfMF8wXzBfMTQxXzFfM19sb2MtMA==",
                        "image": "https://s5.mogucdn.com/mlcdn/c45406/191004_5ad3gj694g3e09hihk8cghbge0jid_640x960.jpg",
                        "title": "秋装新款工装套装女帅气街头bf风飘带酷炫女孩束脚高腰两件套潮",
                        "price": 89.6,
                        "collection": 1828
                    },
                    {
                        "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1mib0zo&acm=3.mce.1_4_1mib0zo.9750.36422.cE47zs1uWzM48.sd_115-swt_69-imt_6-c_2_11_508802481_0_0_3-lc_201-fcid_20003463-mid_9750-pit_24-pm_003-dit_149&cparam=MTU5MTc3OTk3OV8xMWtfN2M2YzAyZDY3MjgwNjZiZjRlY2ZlYzFkNDI0MThkZmJfMTFfMF81MDg4MDI0ODFfNGY4YV8wXzBfMF83MjdfMV8zX2xvYy0w",
                        "image": "https://s5.mogucdn.com/mlcdn/c45406/190613_6lkfc97hfd87lj0ghf123j8leh1kc_640x960.jpg",
                        "title": "2020夏装新款韩版超火cec短袖t恤女宽松学生牛油果绿上衣",
                        "price": 29.9,
                        "collection": 8780
                    },
                    {
                        "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1miyyky&acm=3.mce.1_4_1miyyky.9750.36422.cE47zs1uWzM48.sd_115-swt_69-imt_6-c_2_11_512417019_0_0_3-lc_201-fcid_20003463-mid_9750-pit_24-pm_003-dit_149&cparam=MTU5MTc3OTk3OV8xMWtfN2M2YzAyZDY3MjgwNjZiZjRlY2ZlYzFkNDI0MThkZmJfMTFfMF81MTI0MTcwMTlfNDhfMF8wXzBfOTAwXzFfM19sb2MtMA==",
                        "image": "https://s5.mogucdn.com/mlcdn/c45406/190704_7468ki6kaib5h520h1h240k37ea16_640x960.jpg",
                        "title": "智熏桔梗裙厌世风丧系连衣裙很仙的法式小众山本波点网红抖音裙子",
                        "price": 89.6,
                        "collection": 993
                    },
                    {
                        "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1mipehu&acm=3.mce.1_4_1mipehu.9750.36422.cE47zs1uWzM48.sd_115-swt_69-imt_6-c_2_11_510997717_0_0_3-lc_201-fcid_20003463-mid_9750-pit_24-pm_003-dit_149&cparam=MTU5MTc3OTk3OV8xMWtfN2M2YzAyZDY3MjgwNjZiZjRlY2ZlYzFkNDI0MThkZmJfMTFfMF81MTA5OTc3MTdfNGY4Y18wXzBfMF82MzlfMV8zX2xvYy0w",
                        "image": "https://s5.mogucdn.com/mlcdn/c45406/190627_4bd2il5d76fgle66h111a378c9536_640x854.jpg",
                        "title": "高腰阔腿牛仔裤女2020夏季新款韩版字母拼接宽松显瘦拖地裤子",
                        "price": 79,
                        "collection": 3405
                    },
                    {
                        "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1mfi91u&acm=3.mce.1_4_1mfi91u.9750.36422.cE47zs1uWzM48.sd_115-swt_69-imt_6-c_2_11_495045861_0_0_3-lc_201-fcid_20003463-mid_9750-pit_24-pm_003-dit_149&cparam=MTU5MTc3OTk3OV8xMWtfN2M2YzAyZDY3MjgwNjZiZjRlY2ZlYzFkNDI0MThkZmJfMTFfMF80OTUwNDU4NjFfNGNfMF8wXzBfOTQxXzFfM19sb2MtMA==",
                        "image": "https://s5.mogucdn.com/mlcdn/c45406/190413_802lfgdb2he705g06766h1f9hl852_640x960.jpg",
                        "title": "套装女夏季2020新款韩版洋气上衣牛仔短裤俏皮时尚休闲两件套",
                        "price": 128,
                        "collection": 6826
                    }
                ]
            },
            {
                "page": 1,
                "tabId": 1003,
                "tabName": "新款",
                "item": [
                    {
                        "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1lqnihu&acm=3.mce.1_1_1lqnihu.9750.44188-27059.uQATbs1uXsozb.sd_115-swt_69-imt_7-c_2_11_425174973_0_40_0-lc_201-fcid_20003463-mid_9750-pit_30-c1_3_657278357_10000001-dit_149&cparam=MTU5MTc4MDE4OV8xMWtfMTQ0YWRmNGYzNzQzNWFmYmRmNDAyNDcxYmMyYTYxMWJfMTFfN180MjUxNzQ5NzNfNGRfMF80MF8wXzg5MF8xXzA=",
                        "image": "https://s5.mogucdn.com/mlcdn/c45406/180122_34447515be969k225dc8dbe217fe5_640x960.jpg",
                        "title": "【50片】国妆特证祛斑婴儿蚕丝面膜女锁水保湿细致毛孔面膜贴",
                        "price": 79,
                        "collection": 629
                    },
                    {
                        "link": "https://h5.mogu.com/detail-normal/index.html?itemId=18kpdji&acm=3.mce.1_1_18kpdji.9750.44188-27059.uQATbs1uXsozb.sd_115-swt_69-imt_7-c_2_11_528517537_0_39_0-lc_201-fcid_20003463-mid_9750-pit_30-c1_3_259252811_10000001-dit_149&cparam=MTU5MTc4MDE4OV8xZTI5eTllX2RkNjZlMzM3YzdlZjczZjE3YzYxZjljZjY1YTg4NWQyXzExXzZfNTI4NTE3NTM3XzRkXzBfMzlfMF82OTRfMV8w",
                        "image": "https://s5.mogucdn.com/p2/161020/105269942_1k0fhjh784ia049gjk0ggd5a417li_640x960.png",
                        "title": "925纯银耳钉韩版时尚百搭日韩气质简约淡水珍珠可爱耳钉女",
                        "price": 19.17,
                        "collection": 5360
                    },
                    {
                        "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1mldhq2&acm=3.mce.1_4_1mldhq2.9750.36422.uQATbs1uXsozc.sd_115-swt_69-imt_6-c_2_11_530327605_0_0_3-lc_201-fcid_20003463-mid_9750-pit_24-pm_003-dit_149&cparam=MTU5MTc4MDE4OV8xMWtfMTQ0YWRmNGYzNzQzNWFmYmRmNDAyNDcxYmMyYTYxMWJfMTFfMF81MzAzMjc2MDVfNGNfMF8wXzBfMjI3XzFfM19sb2MtMA==",
                        "image": "https://s5.mogucdn.com/mlcdn/c45406/190926_4k2de458l2ae94dc87gh681gkigh2_3332x4999.jpg",
                        "title": "超显胸春装新款V领交叉薄毛衣紧身性感修身内搭打底衫针织衫女",
                        "price": 39.9,
                        "collection": 2382
                    },
                    {
                        "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1mjx4cg&acm=3.mce.1_4_1mjx4cg.9750.36422.uQATbs1uXsozc.sd_115-swt_69-imt_6-c_2_11_518576321_0_0_3-lc_201-fcid_20003463-mid_9750-pit_24-pm_003-dit_149&cparam=MTU5MTc4MDE4OV8xMWtfMTQ0YWRmNGYzNzQzNWFmYmRmNDAyNDcxYmMyYTYxMWJfMTFfMF81MTg1NzYzMjFfNGVfMF8wXzBfNjA5XzFfM19sb2MtMA==",
                        "image": "https://s5.mogucdn.com/mlcdn/c45406/190807_2273443ad6llk58cl8j979hhf1ja5_640x960.jpg",
                        "title": "春装维多利亚法式复古桔梗长裙很仙法国小众初恋连衣裙气质卫衣裙",
                        "price": 45,
                        "collection": 4006
                    },
                    {
                        "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1mkrkd8&acm=3.mce.1_4_1mkrkd8.9750.36422.uQATbs1uXsozc.sd_115-swt_69-imt_6-c_2_11_524977988_0_0_3-lc_201-fcid_20003463-mid_9750-pit_24-pm_003-dit_149&cparam=MTU5MTc4MDE4OV8xMWtfMTQ0YWRmNGYzNzQzNWFmYmRmNDAyNDcxYmMyYTYxMWJfMTFfMF81MjQ5Nzc5ODhfNGY4ZF8wXzBfMF82NDRfMV8zX2xvYy0w",
                        "image": "https://s5.mogucdn.com/mlcdn/c45406/190906_0e5fdgjl8c72ge1kidl9i8i0ii7kd_640x850.jpg",
                        "title": "秋装套装新款女韩版宽松纯色短款连帽卫衣+高腰破洞牛仔裤两件套",
                        "price": 15.9,
                        "collection": 1394
                    },
                    {
                        "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1mo7kho&acm=3.mce.1_4_1mo7kho.9750.36422.uQATbs1uXsozc.sd_115-swt_69-imt_6-c_2_11_545379338_0_0_3-lc_201-fcid_20003463-mid_9750-pit_24-pm_003-dit_149&cparam=MTU5MTc4MDE4OV8xMWtfMTQ0YWRmNGYzNzQzNWFmYmRmNDAyNDcxYmMyYTYxMWJfMTFfMF81NDUzNzkzMzhfNGNfMF8wXzBfNF8xXzNfbG9jLTA=",
                        "image": "https://s5.mogucdn.com/mlcdn/c45406/191122_5h89la9b64b8ckh5a7j33k0cjbab1_640x960.jpg",
                        "title": "雪纺打底长袖衬衣女春季2020新款设计感气质缎面交叉内搭小衫",
                        "price": 69.3,
                        "collection": 506
                    },
                    {
                        "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1mk5gro&acm=3.mce.1_4_1mk5gro.9750.36422.uQATbs1uXsozc.sd_115-swt_69-imt_6-c_2_11_521696845_0_0_3-lc_201-fcid_20003463-mid_9750-pit_24-pm_003-dit_149&cparam=MTU5MTc4MDE4OV8xMWtfMTQ0YWRmNGYzNzQzNWFmYmRmNDAyNDcxYmMyYTYxMWJfMTFfMF81MjE2OTY4NDVfNGVfMF8wXzBfMjY4XzFfM19sb2MtMA==",
                        "image": "https://s5.mogucdn.com/mlcdn/c45406/190816_5ij8f7ae7h5676k7057dg56b27kb2_640x853.jpg",
                        "title": "50两件露肩修身显瘦打底衫女春秋韩版套头款长袖针织衫紧身上衣",
                        "price": 29.9,
                        "collection": 2941
                    },
                    {
                        "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1mjtnzs&acm=3.mce.1_4_1mjtnzs.9750.36422.uQATbs1uXsozc.sd_115-swt_69-imt_6-c_2_11_517334982_0_0_3-lc_201-fcid_20003463-mid_9750-pit_24-pm_003-dit_149&cparam=MTU5MTc4MDE4OV8xMWtfMTQ0YWRmNGYzNzQzNWFmYmRmNDAyNDcxYmMyYTYxMWJfMTFfMF81MTczMzQ5ODJfNGY4YV8wXzBfMF81MzNfMV8zX2xvYy0w",
                        "image": "https://s5.mogucdn.com/mlcdn/c45406/190804_35eb44fflce9cjj9i11547a3d9h4c_640x854.jpg",
                        "title": "2020春季新款时尚百搭不规则鱼尾裙卫衣拼接牛仔裙连帽连衣裙",
                        "price": 98,
                        "collection": 5812
                    },
                    {
                        "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1mk2oaq&acm=3.mce.1_4_1mk2oaq.9750.36422.uQATbs1uXsozc.sd_115-swt_69-imt_6-c_2_11_519046342_0_0_3-lc_201-fcid_20003463-mid_9750-pit_24-pm_003-dit_149&cparam=MTU5MTc4MDE4OV8xMWtfMTQ0YWRmNGYzNzQzNWFmYmRmNDAyNDcxYmMyYTYxMWJfMTFfMF81MTkwNDYzNDJfNGNfMF8wXzBfMTE0XzFfM19sb2MtMA==",
                        "image": "https://s5.mogucdn.com/mlcdn/c45406/190813_1hf98lh67e1gbbi24ahhb4j2h6k3h_640x960.jpg",
                        "title": "早秋新款女装侧边系带宽松牛仔衬衣打底长袖T恤螺纹打底裤三件套",
                        "price": 49,
                        "collection": 2880
                    },
                    {
                        "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1mq51ig&acm=3.mce.1_4_1mq51ig.9750.36422.uQATbs1uXsozc.sd_115-swt_69-imt_6-c_2_11_555219404_0_0_3-lc_201-fcid_20003463-mid_9750-pit_24-pm_003-dit_149&cparam=MTU5MTc4MDE4OV8xMWtfMTQ0YWRmNGYzNzQzNWFmYmRmNDAyNDcxYmMyYTYxMWJfMTFfMF81NTUyMTk0MDRfNGNfMF8wXzBfNjA5XzFfM19sb2MtMA==",
                        "image": "https://s5.mogucdn.com/mlcdn/c45406/200131_5gf164dd9djcb83afhal33b10fcgh_640x960.jpg",
                        "title": "蕾丝长袖T恤女春季2020宽松韩版学生中长款假两件上衣打底衫",
                        "price": 49.9,
                        "collection": 257
                    }
                ]
            }
        ]
    }

