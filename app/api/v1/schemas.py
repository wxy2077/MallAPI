#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/8 11:33
# @Author  : CoderCharm
# @File    : schemas.py
# @Software: PyCharm
# @Desc    :
"""

验证参数

"""
from typing import Optional
from pydantic import BaseModel, conint


class PageBase(BaseModel):
    """
    page: int 当前页 默认 1
    pageSize: int 当前分页长度 默认 10
    """
    page: int = 1
    pageSize: conint(le=50) = 10  # 限制最大长度小于等于 50 默认10


class HomeGoods(PageBase):
    tabId: int = 0


class Category(PageBase):
    """
    商品分类查询 \n
    tabId: 分类的tabId \n
    """
    tabId: int


class GoodsInfo(BaseModel):
    """
    商品详情Id  \n
    goodsId: 默认 为123 只能传123 \n
    """
    goodsId: int = 123


class UserLogin(BaseModel):
    """
    用户登录
    """
    username: str
    password: str


class TokenPayload(BaseModel):
    sub: Optional[int] = None
