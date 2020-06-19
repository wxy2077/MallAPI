#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/5 17:44
# @Author  : CoderCharm
# @File    : __init__.py.py
# @Software: PyCharm
# @Desc    :
"""

"""

from fastapi import APIRouter

api_v1 = APIRouter()

from api.v1.home import home, home_backup
from api.v1.goods import goods, goods_backup
from api.v1.category import category, category_backup
