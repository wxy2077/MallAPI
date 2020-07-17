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
from fastapi import Depends, APIRouter, Query

from api.v1.database import get_db
from extensions import logger
from utils import response_code

router = APIRouter()


@router.get("/home/banner", summary="首页轮播图")
async def home_banner(db: Session = Depends(get_db)):
    """
    首页轮播图 \n
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


@router.get("/home/features", summary="首页轮播图下的四张图")
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


@router.get("/home/recommends", summary="首页推荐分类")
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


@router.get("/home/tab", summary="首页tab切换的信息")
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


@router.get("/home/goods", summary="tab切换商品信息")
async def home_goods(
        db: Session = Depends(get_db),
        tab_id: int = Query(0, alias="tabId"),
        page: int = 1,
        page_size: int = Query(10, alias="pageSize", le=50)):
    """
    切换的 tab 商品信息\n
    :param db
    :param tab_id 指定的tabId 类型 默认0 全部分类查询前10条\n
    :param page 当前多少页 默认第1页\n
    :param page_size 每页数量 默认10条\n
    :return:
    """
    logger.info("首页商品切换请求正常")

    # 由于limit 从0开始,所以 默认-1
    offset = (page - 1) * page_size
    if tab_id:
        # 查询当前分类到数量
        count_sql = f"select count(1) from mall_goods where tab_id={tab_id}"
        count_data = db.execute(count_sql)
        all_count = count_data.fetchone()[0]
        if all_count <= 0:
            return_data = {
                "msg": f"当前查找的tabID:{tab_id}不存在, /home/tab 此接口获取tabId"
            }
        else:
            sql = f"SELECT link,image,title,price,collection from mall_goods WHERE tab_id={tab_id} order by goods_id desc limit {offset}, {page_size}"

            query_data = db.execute(sql)
            return_data = {
                "item": [],
                "pageInfo": {
                    "allCount": all_count,
                    "page": page,
                    "pageSize": page_size

                }
            }

            for item in query_data:
                temp_data = {
                    "tabId": tab_id,
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
            data_sql = f"""SELECT tab_id,link,image,title,price,collection from mall_goods WHERE tab_id={tab[0]} order by goods_id desc limit 0, {page_size}"""
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
