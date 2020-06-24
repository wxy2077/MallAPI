#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/10 13:39
# @Author  : CoderCharm
# @File    : goods.py
# @Software: PyCharm
# @Desc    :
"""

"""
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from api.v1.database import get_db
from api.v1.schemas import GoodsInfo

from utils import response_code

from utils import custom_exc


router = APIRouter()


@router.post("/goods/detail", summary="商品详情页信息，固定goodsId传123")
async def goods_detail(*, db: Session = Depends(get_db), goods_info: GoodsInfo):
    """
    商品详情页信息 \n
    goodsId 商品id 默认123 额 也只有123哈哈哈 \n
    :param: db
    :param: goods_info
    :return:
    """
    sql = f"""select goods_id, banners, title, price, original_price, sales_volume, sales_collect,sales_deliver, 
    discount_volume, discount_activity, logistics_info, shop_id, goods_image, goods_desc from mall_goods_detail where goods_id={goods_info.goodsId}"""
    goods_res = db.execute(sql)
    info = goods_res.fetchone()
    if not info:
        raise custom_exc.PostParamsError(err_desc=f"数据库没有goodsId为{goods_info.goodsId}的数据")
    data = {
        "goodsId": goods_info.goodsId,
        "banners": str(info[1]).split(","),
        "title": info[2],
        "price": info[3],
        "original_price": info[4],
        "sales_volume": info[5],
        "sales_collect": info[6],
        "sales_deliver": info[7],
        "discount_volume": str(info[8]).split(","),
        "discount_activity": str(info[9]).split(","),
        "logistics_info": str(info[10]).split(","),
        # 11 物流信息
        "goods_image": str(info[12]).split(","),
        "goods_desc": info[13],
    }
    shop_id = info[11]
    shop_sql = f"""select shop_name, shop_image,credit_rating, goods_num, follow, cumulative_sales from mall_shop
            where shop_id={shop_id}"""
    shop_res = db.execute(shop_sql)
    shop_res = shop_res.fetchone()
    shop_info = {
        "shopName": shop_res[0],
        "shopImage": shop_res[1],
        "creditRating": shop_res[2],
        "goodsNum": shop_res[3],
        "follow": shop_res[4],
        "cumulativeSales": shop_res[5],
    }
    data["shopInfo"] = shop_info

    comment_sql = f"""select user_id, comment, buy_info from mall_goods_comment where goods_id={goods_info.goodsId} 
                order by id desc limit 2"""

    comment_res = db.execute(comment_sql)
    comment_res = comment_res.fetchall()
    comment_info = []
    for i in comment_res:
        temp_comment = {
            "userName": "会飞的猪",
            "userImage": "https://s5.mogucdn.com/p1/160105/idid_ifrwenjuhfsggntfguzdambqhayde_160x160.jpg_48x48.webp",
            "comment": i[1],
            "buyInfo": str(i[2]).split(",")
        }
        comment_info.append(temp_comment)
    data["commentInfo"] = comment_info

    # 规格直接偷懒
    data["spec"] = {
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

    return response_code.resp_200(data)
