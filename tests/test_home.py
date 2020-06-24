#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/24 10:48
# @Author  : CoderCharm
# @File    : test_home.py
# @Software: PyCharm
# @Desc    :
"""

测试首页接口数据

"""

from api import create_app
from fastapi.testclient import TestClient

app = create_app()

client = TestClient(app)


def test_banner():
    response = client.get("/api/v1/home/banner")
    assert response.status_code == 200
    assert response.json().get("code") == 200


def test_features():
    response = client.get("/api/v1/home/features")
    assert response.status_code == 200
    assert response.json().get("code") == 200


def test_recommends():
    response = client.get("/api/v1/home/recommends")
    assert response.status_code == 200
    assert response.json().get("code") == 200


def test_tab():
    response = client.get("/api/v1/home/tab")
    assert response.status_code == 200
    assert response.json().get("code") == 200


def test_goods():
    response = client.get(
        "/api/v1/home/goods",
        params={
            "tabId": 0,
            "page": 1,
            "pageSize": 10
        }
    )
    assert response.status_code == 200
    assert response.json().get("code") == 200


if __name__ == '__main__':
    test_banner()
    test_features()
    test_recommends()
    test_tab()
    test_goods()
