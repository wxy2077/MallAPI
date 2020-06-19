#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/9 14:47
# @Author  : CoderCharm
# @File    : development_config.py
# @Software: PyCharm
# @Desc    :
"""
开发环境配置

"""
from typing import Union
from pydantic import AnyHttpUrl, BaseSettings, IPvAnyAddress


class Config(BaseSettings):

    # 配置你的Mysql环境
    MYSQL_USERNAME: str = 'root'
    MYSQL_PASSWORD: str = "Admin12345-"
    MYSQL_HOST: Union[AnyHttpUrl, IPvAnyAddress] = "172.16.137.129"
    MYSQL_DATABASE: str = 'Mall'


config = Config()
