#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/24 11:15
# @Author  : CoderCharm
# @File    : test_category.py
# @Software: PyCharm
# @Desc    :
"""

测试分类模块

"""

from api import create_app
from fastapi.testclient import TestClient

app = create_app()

client = TestClient(app)


def test_category():
    response = client.get("/api/v1/category")
    assert response.status_code == 200
    print(response.json())
    assert response.json().get("code") == 200


def test_category_tab():
    response = client.get(
        "/api/v1/category/tab",
        params={"cateId": 1}
    )
    assert response.status_code == 200
    print(response.json())
    assert response.json().get("code") == 200


def test_category_goods():
    response = client.post(
        "/api/v1/category/goods",
        json={
            "page": 1,
            "pageSize": 10,
            "cateId": 1,
            "tabId": 1005
        }
    )
    assert response.status_code == 200
    print(response.json())
    assert response.json().get("code") == 200


if __name__ == '__main__':
    test_category()
    test_category_tab()
    test_category_goods()
