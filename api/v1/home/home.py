#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/5 17:48
# @Author  : CoderCharm
# @File    : home.py
# @Software: PyCharm
# @Desc    :
"""

"""

from sqlalchemy.orm import Session
from fastapi import Depends

from api.v1.database import get_db
from api.v1 import api_v1
from extensions import logger
from utils import response_code


@api_v1.get("/home/banner", tags=["首页"], summary="首页轮播图")
async def home_banner(db: Session = Depends(get_db)):
    """
    首页轮播图
    :return: 轮播图banner link, image
    """

    sql = "select link,image from mall_banner order by id desc limit 10"
    banner_info = db.execute(sql)
    banner_data = []
    for banner in banner_info:
        temp_data = {
            "link": banner[0],
            "image": banner[1]
        }
        banner_data.append(temp_data)

    return response_code.resp_200(banner_data)


@api_v1.get("/home/features", tags=["首页"], summary="首页轮播图下的四张图")
async def home_features(db: Session = Depends(get_db)):
    """
    首页特色 features \n
    :return: 返回features信息 link, image, title
    """
    sql = "select link,features_image,title from mall_goods where is_features=1 order by goods_id desc limit 4"
    query_data = db.execute(sql)

    return_data = []
    for item in query_data:
        temp_data = {
            "link": item[0],
            "image": item[1],
            "title": item[2]
        }
        return_data.append(temp_data)

    return response_code.resp_200(return_data)


@api_v1.get("/home/recommends", tags=["首页"], summary="首页推荐分类, 原视频是一张整图")
async def home_recommends(db: Session = Depends(get_db)):
    """
    首页推荐 recommends \n
    :return: 推荐信息: cateId, cateName, image
    """
    sql = "select cate_id,cate_name,cate_thumbnail from mall_goods_cate order by id desc limit 8"
    query_data = db.execute(sql)

    return_data = []
    for item in query_data:
        temp_data = {
            "cateId": item[0],
            "cateName": item[1],
            "image": item[2]
        }
        return_data.append(temp_data)

    return response_code.resp_200(return_data)


@api_v1.get("/home/tab", tags=["首页"], summary="首页tab切换的信息")
async def goods_tab(db: Session = Depends(get_db)):
    """
    切换的tab信息 \n
    :return:
    """
    sql = "SELECT tab_id,tab_name from mall_tab WHERE is_home=1"
    query_data = db.execute(sql)

    return_data = []
    for item in query_data:
        temp_data = {
            "tabId": item[0],
            "tabName": item[1],
        }
        return_data.append(temp_data)

    return response_code.resp_200(return_data)


@api_v1.get("/home/goods", tags=["首页"], summary="tab切换商品信息")
async def home_goods(db: Session = Depends(get_db), tabId: int = 0, page: int = 1, pageSize: int = 10):
    """
    切换的 tab 商品信息\n
    :param tabId 指定的tabId 类型 默认0 全部分类查询前10条\n
    :param page 当前多少页 默认第1页\n
    :param pageSize 每页数量 默认10条\n
    :return:
    """
    logger.info("首页商品切换请求正常")

    # 由于limit 从0开始,所以 默认-1
    offset = (page - 1) * pageSize
    if tabId:
        # 查询当前分类到数量
        count_sql = f"select count(1) from mall_goods where tab_id={tabId}"
        count_data = db.execute(count_sql)
        all_count = count_data.fetchone()[0]
        if all_count <= 0:
            return_data = {
                "msg": f"当前查找的tabID:{tabId}不存在, /home/tab 此接口获取tabId"
            }
        else:
            sql = f"SELECT link,image,title,price,collection from mall_goods WHERE tab_id={tabId} order by goods_id desc limit {offset}, {pageSize}"

            query_data = db.execute(sql)
            return_data = {
                "item": [],
                "pageInfo": {
                    "allCount": all_count,
                    "page": page,
                    "pageSize": pageSize

                }
            }

            for item in query_data:
                temp_data = {
                    "tabId": tabId,
                    "link": item[0],
                    "image": item[1],
                    "title": item[2],
                    "price": item[3],
                    "collection": item[4],
                }
                return_data["item"].append(temp_data)
    else:
        # 默认查询全部分类 的前10条记录
        sql = "SELECT tab_id,tab_name from mall_tab WHERE is_home=1"
        tab_res = db.execute(sql)
        # 查询出每个分类的前10条数据
        # Tip: 我SQL 好弱 花了快1小时没解决,放弃，用笨办法  搜到这个也没解决https://stackoverflow.com/questions/12113699/get-top-n-records-for-each-group-of-grouped-results
        return_data = []
        # 循环每个tab
        for tab in tab_res.fetchall():
            data_sql = f"""SELECT tab_id,link,image,title,price,collection from mall_goods WHERE tab_id={tab[0]} order by goods_id desc limit 0, {pageSize}"""
            query_data = db.execute(data_sql)
            goods_item = {
                "page": 1,
                "tabId": tab[0],
                "tabName": tab[1],
                "item": [],
            }
            for goods in query_data:
                temp_goods = {
                    "link": goods[1],
                    "image": goods[2],
                    "title": goods[3],
                    "price": goods[4],
                    "collection": goods[5],
                }
                goods_item["item"].append(temp_goods)
            return_data.append(goods_item)

    return response_code.resp_200(return_data)
