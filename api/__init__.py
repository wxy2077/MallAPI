#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/5 17:36
# @Author  : CoderCharm
# @File    : __init__.py.py
# @Software: PyCharm
# @Desc    :
"""
模仿flask 工厂模式目录结构

"""
import traceback

from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware


from api.v1 import api_v1
from extensions import logger
from utils import  response_code
from utils.custom_exc import PostParamsError

# swigger 文档分类 https://fastapi.tiangolo.com/tutorial/metadata/
tags_metadata = [
    {
        "name": "首页",
        "description": "首页数据",
    },
    {
        "name": "详情",
        "description": "详情页数据",
    },
    {
        "name": "分类",
        "description": "分类数据",
    },
    {
        "name": "备份",
        "description": "备份信息",
    },
]


def create_app():
    app = FastAPI(
        title="FastAPI",
        description="更多信息查看https://www.charmcode.cn/article/2020-06-08_vue_mall_api ",
        version="0.1.1",
        openapi_tags=tags_metadata
    )

    app.include_router(
        api_v1,
        prefix="/api/v1",
        # tags=["items"],
        # dependencies=[Depends(get_token_header)],
        # responses={404: {"description": "Not found"}},
    )

    register_exception(app)
    return app


def register_exception(app: FastAPI):
    """
    全局异常捕获
    :param app:
    :return:
    """
    # 捕获自定义异常
    @app.exception_handler(PostParamsError)
    async def unicorn_exception_handler(request: Request, exc: PostParamsError):
        return JSONResponse(
            status_code=418,
            content={"code": 400, "data": {"tip": exc.err_desc}, "status": "fail"},
        )

    # 捕获参数 验证错误
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        logger.error(f"参数错误: \n{traceback.format_exc()}")
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=jsonable_encoder({"code": 400, "data": {"tip": exc.errors()}, "body": exc.body, "status": "fail"}),
        )

    # 捕获全部异常
    @app.exception_handler(Exception)
    async def all_exception_handler(request: Request, exc: Exception):
        logger.error(f"全局异常: \n{traceback.format_exc()}")
        return JSONResponse(
            status_code=418,
            content={"code": 500, "data": {"tip": "服务器错误"}, "status": "fail"},
        )


def register_cors(app):
    """
    支持跨域

    貌似发现了一个bug
    https://github.com/tiangolo/fastapi/issues/133

    :param app:
    :return:
    """

    app.add_middleware(
        CORSMiddleware,
        # allow_origins=['http://localhost:8081'],  # 有效, 但是本地vue端口一直在变化, 接口给其他人用也不一定是这个端口
        # allow_origins=['*'],   # 无效 bug allow_origins=['http://localhost:8081']
        allow_origin_regex='https?://.*',   # 改成用正则就行了
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

