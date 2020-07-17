#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/16 16:05
# @Author  : CoderCharm
# @File    : goods_backup.py
# @Software: PyCharm
# @Desc    :
"""

"""

from fastapi import APIRouter


router = APIRouter()


@router.post("/goods/detail/backup", summary="商品详情,备份信息")
async def goods_detail():
    """
    商品详情页信息备份 \n
    :param: goodsId 商品id 默认123 额 也只有123哈哈哈 \n
    :return:
    """
    return {
        "code": 200,
        "msg": "ok",
        "data": {
            "goodsId": 123,
            "banners": [
                "https://s11.mogucdn.com/mlcdn/c45406/170919_6h807cjg6c6e065kkalf9gh620aj7_640x960.jpg_640x960.v1cAC.70.webp",
                "https://s5.mogucdn.com/mlcdn/c45406/170919_30a5je68053hf31h24610gedbk64h_640x960.jpg_640x960.v1cAC.70.webp",
                "https://s5.mogucdn.com/mlcdn/c45406/170919_6h996g6jjd1j226kl3f553986347c_640x960.jpg_640x960.v1cAC.70.webp",
                "https://s5.mogucdn.com/mlcdn/c45406/170919_6fkag39hdd5j4ffaeek99hg4g203g_640x960.jpg_640x960.v1cAC.70.webp"
            ],
            "title": "【秋衣女】外穿打底衫女长袖中长款上衣春装新款小衫韩版学生宽松T恤",
            "price": 59.9,
            "original_price": 109.9,
            "sales_volume": 1031,
            "sales_collect": 3100,
            "sales_deliver": "72小时内发货",
            "discount_volume": [
                "满99减2",
                "满120减5"
            ],
            "discount_activity": [
                "买三件送一件"
            ],
            "logistics_info": [
                "退货补运费",
                "全国包邮",
                "七天无理由退货"
            ],
            "goods_image": [
                "https://s11.mogucdn.com/mlcdn/c45406/170919_81fae35fccie4akl4igg64g4lc8cl_744x850.jpg_468x468.webp",
                "https://s11.mogucdn.com/mlcdn/c45406/170919_23eib586jf6egg0ihc93045461a29_744x850.jpg_468x468.webp",
                "https://s5.mogucdn.com/mlcdn/c45406/170919_8070cehgi7dj80a83fa5ki7b41i5k_744x850.jpg_468x468.webp",
                "https://s11.mogucdn.com/mlcdn/c45406/170919_48j5023igk9clefc92c7fkjk8ei12_744x850.jpg_468x468.webp",
                "https://s5.mogucdn.com/mlcdn/c45406/170919_37c9gidl48a12l25l16d39l1i9le3_744x850.jpg_468x468.webp",
                "https://s11.mogucdn.com/mlcdn/c45406/170919_56ag21bbgjelab2g0h97bbe7f5jgi_744x850.jpg_468x468.webp",
                "https://s11.mogucdn.com/mlcdn/c45406/170919_88i68ailg6fl53075k1el95b0i7ga_744x850.jpg_468x468.webp",
                "https://s5.mogucdn.com/mlcdn/c45406/170919_82j9af1i5ljdlelebjjl753193269_744x850.jpg_468x468.webp",
                "https://s5.mogucdn.com/mlcdn/c45406/170919_44b259b21k28gi160a10jdcl0cefi_744x850.jpg_468x468.webp",
                "https://s5.mogucdn.com/mlcdn/c45406/170919_6k5818g1akijb2k2b3h1a81bb0gif_744x850.jpg_468x468.webp",
                "https://s5.mogucdn.com/mlcdn/c45406/170919_6k5818g1akijb2k2b3h1a81bb0gif_744x850.jpg_468x468.webp"
            ],
            "goods_desc": "每天3点前下单，基本都是可以当天发货的哦。 还有7天时间无理由包退换，我们是免费送运费险的。让亲们可以无忧无虑的购买。（谢谢支持）",
            "shopInfo": {
                "shopName": "浓香公主",
                "shopImage": "https://s5.mogucdn.com/mlcdn/c45406/190515_3defc7eak01l8eag9idkbeaa22bjd_200x200.jpg_120x120.webp",
                "creditRating": "5",
                "goodsNum": 135130,
                "follow": 31000,
                "cumulativeSales": 2312412
            },
            "commentInfo": [
                {
                    "userName": "会飞的猪",
                    "userImage": "https://s5.mogucdn.com/p1/160105/idid_ifrwenjuhfsggntfguzdambqhayde_160x160.jpg_48x48.webp",
                    "comment": "看着还行，穿着很舒服",
                    "buyInfo": [
                        "178cm",
                        "55kg"
                    ]
                },
                {
                    "userName": "会飞的猪",
                    "userImage": "https://s5.mogucdn.com/p1/160105/idid_ifrwenjuhfsggntfguzdambqhayde_160x160.jpg_48x48.webp",
                    "comment": "衣服收到了，很合适",
                    "buyInfo": [
                        "170cm",
                        "45kg"
                    ]
                }
            ],
            "spec": {
                "info": {
                    "set": {
                        "厚薄": "普通",
                        "颜色": "黄色套装",
                        "尺码": "S,XL,L,M,XXL",
                        "衣长": "常规款（51-65cm）",
                        "季节": "夏季",
                        "材质": "其他",
                        "领型": "其他领型",
                        "袖长": "五分袖（中袖）",
                        "款式": "衣裤套装",
                        "风格": "简约"
                    },
                    "key": "产品参数",
                    "anchor": "product_info"
                },
                "rule": {
                    "tables": [
                        [
                            [
                                "尺码",
                                "胸围",
                                "腰围",
                                "袖长",
                                "肩宽"
                            ],
                            [
                                "S",
                                "96",
                                "64",
                                "31",
                                "36"
                            ],
                            [
                                "M",
                                "100",
                                "68",
                                "32",
                                "37"
                            ],
                            [
                                "L",
                                "104",
                                "72",
                                "33",
                                "38"
                            ],
                            [
                                "XL",
                                "108",
                                "76",
                                "34",
                                "39"
                            ],
                            [
                                "XXL",
                                "112",
                                "80",
                                "35",
                                "40"
                            ]
                        ]
                    ],
                    "key": "尺码说明",
                    "anchor": "size_info",
                    "disclaimer": "※ 以上尺寸为实物人工测量，因测量方式不同会有1-2cm误差，相关数据仅作参考，以收到实物为准。"
                }
            }
        }
    }
