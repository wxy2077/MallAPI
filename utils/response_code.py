#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/19 16:12
# @Author  : CoderCharm
# @File    : response_code.py
# @Software: PyCharm
# @Desc    :
"""
定义返回的状态
"""

from typing import Union


def resp_200(data: Union[list, dict, str]) -> dict:
    return {
        'code': 200,
        'message': "Success",
        'data': data,
    }


def resp_403(data: str = None) -> dict:
    return {
        'code': 403,
        'message': "403 forbidden",
        'data': data,
    }


def resp_404(data: str = None) -> dict:
    return {
        'code': 404,
        'message': "Page Not Found",
        'data': data,
    }


def resp_500(data: str = None) -> dict:
    return {
        'code': "500",
        'message': "Server internal error",
        'data': data,
    }


# 自定义
def resp_5000(data: str = None) -> dict:
    return {
        'code': 5000,
        'message': "Invalid parameter",
        'data': data,
    }
