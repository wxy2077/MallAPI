#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/24 10:42
# @Author  : CoderCharm
# @File    : test_docs.py
# @Software: PyCharm
# @Desc    :
"""

测试文档地址是否正确

"""

from api import create_app
from fastapi.testclient import TestClient

app = create_app()

client = TestClient(app)


def test_read_docs():
    docs_response = client.get("/api/v1/docs")
    assert docs_response.status_code == 200


def test_docs_api():
    api_response = client.get("/api/v1/openapi.json")
    assert api_response.status_code == 200


if __name__ == '__main__':
    test_read_docs()
    test_docs_api()
