## 使用FastAPI 构建的商城项目API

> 学习FastAPI 构建项目目录

构建项目接口: [对应博客](https://www.charmcode.cn/article/2020-06-08_vue_mall_api):https://www.charmcode.cn/article/2020-06-08_vue_mall_api

## 声明
此项目已经不再维护, 可以参考我另外一个项目[https://github.com/CoderCharm/fastapi-mysql-generator](https://github.com/CoderCharm/fastapi-mysql-generator)

> 本来使用FastAPI写接口是为了配合我学习Vue顺手看着文档学的，没想到这么多老哥关注，上面那个项目我会尽可能更新完善，一起加油学习吧！！🤪

#### 环境
![Python版本](https://img.shields.io/badge/Python-3.7+-brightgreen.svg "版本号")
![FastAPI版本](https://img.shields.io/badge/FastAPI-0.55.1-ff69b4.svg "版本号")

## 项目文件结构

> 文件结构是仿照Flask项目目录构建的，官方推荐的模版对我而言太大。

官方有推荐项目文件模版  https://fastapi.tiangolo.com/tutorial/bigger-applications/


<details>
<summary>项目文件结构</summary>

```
.
|_app                           // 主项目文件
| 
|___api
| |_____init__.py               // (重要)工厂模式生成app对象
| |____v1
| |____database.py              // 数据库对象
| |____schemas.py               // 验证参数       （可放到对应模块内)
| |____models.py                // models模型类型 （可放到对应模块内)
| |____home                     // 项目模块文件
| | |____home.py
| | |______init__.py
| | |____home_backup.py
| |____category
| | |______init__.py
| |______init__.py
| |____profile
| | |____profile.py
| | |______init__.py
| |____goods
|   |____goods.py
|   |____goods_backup.py
|____test                     // 测试用例
| |______init__.py
| |____test_sqlite.py
|____utils                    // 工具类
| |______init__.py
| |___response_code.py        // 自定义返回的状态码
|____setting                  // 配置文件夹
| |______init__.py            // 根据虚拟环境 导出不同配置
| |____development_config.py  // 开发环境配置
| |____production_config.py   // 生产环境配置
|____extensions               // 扩展文件
| |______init__.py            // 导出扩展文件
| |____logger.py              // 
|____alembic                  //   alembic  初始化自动生成的 
| |____script.py.mako
| |____env.py
| |____versions
| |____README
|____alembic.ini              // alembic  初始化自动生成的 
|____.gitignore
|____requirements.text        // 依赖文件
|____main.py                  // 项目启动文件
|____mall_data.sql            // mysql insert 数据
|____mall_table.sql           // msyql表格 
|____README.md
|____Pipfile
|____Pipfile.lock

```

</details>

## 配置环境
> setting目录下 \_\_init__.py文件，会根据`ENV`的环境变量 导入不同的环境

development_config.py  // 开发环境配置
production_config.py   // 生产环境配置

如果不配置, 就只能访问 backup 备份的接口

## 导入数据

- mall_data.sql            // mysql insert 数据
- mall_table.sql           // msyql表格 

> 上面两个文件是mysql数据， 需自行导入

## 常规启动

#### 安装依赖
```
# 推荐先安装pipenv
pip install pipenv -i https://mirrors.aliyun.com/pypi/simple/

# 先进入到项目文件下
cd /项目目录/MallAPI

# 安装pipenv python版本3.7+
pipenv install --python 3.7 # 注意 --python空格3.7

# 安装完后激活环境
pipenv shell

# 安装依赖
pip install -r requirements.text -i https://mirrors.aliyun.com/pypi/simple/

```

#### 启动

```
cd /项目目录/MallAPI

# 在main.py文件同级目录下 执行
uvicorn main:app --host=127.0.0.1 --port=8010 --reload
```

当然也可以直接执行

```
python main.py
```

## Docker 启动

#### 构建镜像

可以参考FastAPI作者tiangolo构建的镜像

https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker

镜像名字随便取的, 继承FastAPI作者构建的镜像

```shell
docker build -t mallapp .

```

临时测试运行
```shell
docker run -d --name mycontainer -p 8030:8030 mallapp
```

后台运行启动

```shell
docker run -d --name mycontainer -p 80:80 mallapp
```

## 启动后API文档地址

http://127.0.0.1:8010/api/v1/docs    


## 线上文档地址

https://www.charmcode.cn/api/v1/docs


## sqlalchemy + alembic数据迁移

> 尝试使用sqlalchemy + alembic 但是之前使用的Flask-Sqlalchemy扩展，迁移数据库很方便，
研究这个感觉很麻烦，算了直接使用sql语句，数据表手动创建

```
# 安装
pip install alembic

# 初始化 生成alembic配置文件
alembic init alembic
```

具体使用 sqlalchemy 可以参考我这个后台管理的Demo

https://github.com/CoderCharm/FastAdmin/tree/master/backend



#### 参考
- [官方多文件项目组织推荐](https://fastapi.tiangolo.com/tutorial/bigger-applications/) https://fastapi.tiangolo.com/tutorial/bigger-applications/
 
- [官方推荐项目生成模版](https://github.com/tiangolo/full-stack-fastapi-postgresql) https://github.com/tiangolo/full-stack-fastapi-postgresql

- 框架对比 https://fastapi.tiangolo.com/alternatives/#flask

- [awesome-fastapi](https://github.com/mjhea0/awesome-fastapi) https://github.com/mjhea0/awesome-fastapi

- [fastapi-realworld-example-app](https://github.com/nsidnev/fastapi-realworld-example-app/blob/master/Dockerfile) https://github.com/nsidnev/fastapi-realworld-example-app/blob/master/Dockerfile
