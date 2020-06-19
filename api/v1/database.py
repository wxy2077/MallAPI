#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/6 19:23
# @Author  : CoderCharm
# @File    : database.py
# @Software: PyCharm
# @Desc    :
"""

使用MySql数据库

pip install alembic

alembic init alembic

"""
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from setting import config

# Mysql地址
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{config.MYSQL_USERNAME}:{config.MYSQL_PASSWORD}@" \
                          f"{config.MYSQL_HOST}/{config.MYSQL_DATABASE}?charset=utf8mb4"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
