#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/24 10:59
# @Author  : CoderCharm
# @File    : test_goods.py
# @Software: PyCharm
# @Desc    :
"""

测试商品详模块


"""

from api import create_app
from fastapi.testclient import TestClient

app = create_app()

client = TestClient(app)


def test_goods():
    response = client.post("/api/v1/goods/detail", json={"goodsId": 123})
    assert response.status_code == 200
    assert response.json().get("code") == 200


if __name__ == '__main__':
    test_goods()


