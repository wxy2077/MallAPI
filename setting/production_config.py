#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/16 10:15
# @Author  : CoderCharm
# @File    : production_config.py
# @Software: PyCharm
# @Desc    :
"""

生产环境

"""

from typing import Union
from pydantic import AnyHttpUrl, BaseSettings, IPvAnyAddress


class Config(BaseSettings):

    MYSQL_USERNAME: str = 'root'
    MYSQL_PASSWORD: str = ""
    MYSQL_HOST: Union[AnyHttpUrl, IPvAnyAddress] = ""
    MYSQL_DATABASE: str = 'Mall'


config = Config()
