#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/5 17:36
# @Author  : CoderCharm
# @File    : main.py
# @Software: PyCharm
# @Desc    :
"""

pip install uvicorn

# 推荐启动方式
uvicorn main:app --host=127.0.0.1 --port=8010 --reload


类似flask 工厂模式创建

# 生产启动
nohup uvicorn main:app --host=127.0.0.1 --port=8010 > log/error.log 2>&1 &

"""


from api import create_app

app = create_app()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app='main:app', host="127.0.0.1", port=8010, reload=True, debug=True)
