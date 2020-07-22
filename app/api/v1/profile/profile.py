#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/5 17:47
# @Author  : CoderCharm
# @File    : profile.py
# @Software: PyCharm
# @Desc    :
"""

"""
from typing import Any, Union
from datetime import timedelta
# from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from api.v1.schemas import UserLogin
from setting import config
from core import security
from utils import response_code


router = APIRouter()


@router.post("/profile/login", summary="登录")
async def profile_login(user_info: UserLogin):
    """
    登录 \n
    username admin \n
    password 12345 \n
    :param user_info:
    :return:
    """
    # 由于这里这是模拟 所以就不查询数据库了, 如有需要查看我这个项目 FastAPI jwt登录认证
    # https://github.com/CoderCharm/FastAdmin/blob/master/backend/app/api/api_v1/auth/views.py#L32
    if user_info.username == "admin" and user_info.password == "12345":
        # 过期时间
        access_token_expires = timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
        # 保存数据到token中, 我这里保存的是用户名 一般保存用户id
        token = security.create_access_token(user_info.username, expires_delta=access_token_expires)
        return response_code.resp_200({"token": token})
    else:
        return response_code.resp_200(message="用户名或者密码错误")


@router.post("/profile/info", summary="用户信息")
async def profile_info(token_data: Union[str, Any] = Depends(security.check_jwt_token)):
    """
    获取用户信息
    :param token_data:
    :return:
    """
    return response_code.resp_200(data={
        "username": "admin",
        "avatar": "https://pic.cnblogs.com/avatar/1301088/20190724105415.png"
    })




