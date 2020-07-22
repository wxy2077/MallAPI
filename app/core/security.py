#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/22 16:33
# @Author  : CoderCharm
# @File    : security.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""
token password 验证

pip install python-jose

pip install passlib

"""
from datetime import datetime, timedelta
from typing import Any, Union, Optional
from jose import jwt
from passlib.context import CryptContext

from fastapi import Header
from pydantic import ValidationError

from api.v1.schemas import TokenPayload
from setting import config
from utils import custom_exc
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


ALGORITHM = "HS256"


def create_access_token(
    subject: Union[str, Any], expires_delta: timedelta = None
) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, config.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def check_jwt_token(
     token: Optional[str] = Header(None)
) -> Union[str, Any]:
    """
    只解析验证token
    :param token:
    :return:
    """

    try:
        payload = jwt.decode(
            token,
            config.SECRET_KEY, algorithms=[ALGORITHM]
        )
        return payload
    except (jwt.JWTError, ValidationError, AttributeError):
        raise custom_exc.TokenAuthError(err_desc="access token fail")
