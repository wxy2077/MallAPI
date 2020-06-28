#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/18 15:10
# @Author  : CoderCharm
# @File    : category.py
# @Software: PyCharm
# @Desc    :
"""

分类

"""
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from api.v1.database import get_db
from api.v1.schemas import Category
from utils import response_code

router = APIRouter()


@router.get("/category", summary="分类左边列表")
async def get_category(db: Session = Depends(get_db)):
    """

    :param db:
    :return:
    """
    sql = "select cate_id,cate_name,cate_thumbnail from mall_goods_cate"
    goods_info = db.execute(sql)
    info = goods_info.fetchall()

    return response_code.resp_200(info)


@router.get("/category/tab", summary="分类tab选项")
async def category_tab(db: Session = Depends(get_db), *, cate_id: int=Query(1, alias="cateId", title="分类Id")):
    """
    查询分类的 tab 信息 \n
    需要 /category 接口返回的cateId参数 \n
    :param db:  \n
    :param cate_id: int 需要传入分类id 目前数据库只有分类 1 有数据 \n
    :return:
    """
    sql = f"SELECT tab_id,tab_name from mall_tab WHERE cate_id={cate_id}"
    goods_info = db.execute(sql)
    info = goods_info.fetchall()

    return response_code.resp_200(info)


@router.post("/category/goods", summary="分类 选项goods")
async def category_goods(db: Session = Depends(get_db), *, category: Category):
    """
    获取分类数据信息 \n
    cateId: int 分类id \n
    tabId: int  分类的tabId \n
    page  int 分页  \n
    pageSize int 分页长度 \n
    :param db:  \n
    :param category:
    :return:
    """
    # 由于limit 从0开始,所以 默认-1
    offset = (category.page - 1) * category.pageSize

    sql = f"SELECT link,image,title,price,collection from mall_goods WHERE tab_id={category.tabId} order by goods_id desc limit {offset}, {category.pageSize}"
    goods_info = db.execute(sql)
    items = goods_info.fetchall()

    count_sql = f"select count(1) from mall_goods where tab_id={category.tabId}"
    count_data = db.execute(count_sql)
    all_count = count_data.fetchone()[0]

    return_data = {
        "items": items,
        "pageInfo": {
            "allCount": all_count,
            "page": category.page,
            "pageSize": category.pageSize
        }
    }
    return response_code.resp_200(return_data)
