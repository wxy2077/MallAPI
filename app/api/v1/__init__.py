#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/5 17:44
# @Author  : CoderCharm
# @File    : __init__.py.py
# @Software: PyCharm
# @Desc    :
"""

路由汇总

"""

from fastapi import APIRouter
from api.v1.home import home, home_backup
from api.v1.goods import goods, goods_backup
from api.v1.category import category, category_backup
from api.v1.profile import profile

api_v1 = APIRouter()

api_v1.include_router(home.router, tags=["首页API"])
api_v1.include_router(goods.router, tags=["商品API"])
api_v1.include_router(category.router, tags=["分类API"])
api_v1.include_router(profile.router, tags=["个人信息"])


api_v1.include_router(home_backup.router, tags=["备份API"])
api_v1.include_router(goods_backup.router, tags=["备份API"])
api_v1.include_router(category_backup.router, tags=["备份API"])



