#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/6 19:23
# @Author  : CoderCharm
# @File    : database.py
# @Software: PyCharm
# @Desc    :
"""

使用MySql数据库

可参考官网:
https://fastapi.tiangolo.com/tutorial/sql-databases/#create-the-sqlalchemy-parts

pip install alembic

alembic init alembic

"""
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from setting import config

engine = create_engine(
    config.SQLALCHEMY_DATABASE_URI
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
