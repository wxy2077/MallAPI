#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/19 15:51
# @Author  : CoderCharm
# @File    : category_backup.py
# @Software: PyCharm
# @Desc    :
"""

"""

from fastapi import APIRouter
from api.v1.schemas import Category

router = APIRouter()


@router.get("/category/backup", summary="分类左边列表")
async def get_category():
    return {
        "code": 200,
        "msg": "success",
        "data": [
            {
                "cate_id": 1,
                "cate_name": "女装",
                "cate_thumbnail": "https://s10.mogucdn.com/mlcdn/c45406/200327_50ieadafgg13667jgf432hb2ijl9i_135x135.jpg_640x640.v1cAC.40.webp"
            },
            {
                "cate_id": 2,
                "cate_name": "上衣",
                "cate_thumbnail": "https://s10.mogucdn.com/mlcdn/c45406/190903_0572el03440fllf207k3g5kfe6g35_150x150.jpg_640x640.v1cAC.40.webp"
            },
            {
                "cate_id": 3,
                "cate_name": "裤子",
                "cate_thumbnail": "https://s10.mogucdn.com/mlcdn/c45406/191021_2cagf3kgj81d6895k8571g8jbj30e_135x135.jpg_640x640.v1cAC.40.webp"
            },
            {
                "cate_id": 4,
                "cate_name": "裙子",
                "cate_thumbnail": "https://s10.mogucdn.com/mlcdn/c45406/200327_1a3d2egbb3cagj7cg9jk8k5e24ck2_135x135.jpg_640x640.v1cAC.40.webp"
            },
            {
                "cate_id": 5,
                "cate_name": "套装",
                "cate_thumbnail": "https://s10.mogucdn.com/mlcdn/c45406/200525_7lj1302k99cbh22ad37aild2c9b5a_135x135.jpg_640x640.v1cAC.40.webp"
            },
            {
                "cate_id": 6,
                "cate_name": "家居",
                "cate_thumbnail": "https://s10.mogucdn.com/mlcdn/c45406/200327_60hgbe9a54jd413df21l3gb468fa0_135x135.jpg_640x640.v1cAC.40.webp"
            },
            {
                "cate_id": 7,
                "cate_name": "男装",
                "cate_thumbnail": "https://s10.mogucdn.com/mlcdn/c45406/200327_691e4fja6j2heh0egge060hfj7372_135x135.jpg_640x640.v1cAC.40.webp"
            },
            {
                "cate_id": 8,
                "cate_name": "童装",
                "cate_thumbnail": "https://s10.mogucdn.com/mlcdn/c45406/200327_0kllejc8c75ak5a942jd5f56ghh19_135x135.jpg_640x640.v1cAC.40.webp"
            }
        ]
    }


@router.get("/category/tab/backup", summary="分类tab选项")
async def category_tab(cateId: int = 1):
    """
    查询分类的 tab 信息 \n
    需要 /category 接口返回的cateId参数 \n
    :param cateId: int 需要传入分类id \n
    :return:
    """
    return {
        "code": 200,
        "msg": "success",
        "data": [
            {
                "tab_id": 1004,
                "tab_name": "精选女装"
            },
            {
                "tab_id": 1005,
                "tab_name": "初秋上新"
            },
            {
                "tab_id": 1006,
                "tab_name": "时尚达人"
            }
        ]
    }


@router.post("/category/goods/backup", summary="分类 选项goods")
async def category_goods(category: Category):
    """
    获取分类数据信息 \n
    cateId: int 分类id  测试参数 1 \n
    tabId: int  分类的tabId 测试参数 1004 1005 1006三个中的一个 \n
    page  int 分页  \n
    pageSize int 分页长度 \n
    :param category:
    :return:
    """
    return {
        "code": 200,
        "msg": "success",
        "data": {
            "items": [
                {
                    "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1mtnj7m&acm=3.ms.1_4_1mtnj7m.46.36613-93872-68998.dQSxjs2fTg747.sd_117-swt_46-imt_6-c_1_17_576256327_0_0_3-t_mLA6Hs2fSXRlg-lc_17-pit_1-qid_90128-dit_&cparam=MTU5MjQ3MzY3N18xMWtfNmJiMDI5MjE2ZGVjODVhMDUzYjJmMzcyZjk1YTc4NTNfMTdfMF81NzYyNTYzMjdfNDhfMF8wXzBfMTI5XzFfM19sb2MtMA==",
                    "image": "https://s5.mogucdn.com/mlcdn/776a41/200617_66693743lk6b6a913gka9i3fldljk_750x1125.jpg",
                    "title": "夏季新款小个子减龄遮肚子紫色牛仔背带裤雪纺泡泡袖上衣两件套女",
                    "price": 43.4,
                    "collection": 76
                },
                {
                    "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1mrydwm&acm=3.ms.1_4_1mrydwm.46.36613-93872-68998.dQSxjs2fTg747.sd_117-swt_46-imt_6-t_mLA6Hs2fSXRlg-lc_17-pit_1-qid_90128-dit_",
                    "image": "https://s5.mogucdn.com/mlcdn/776a41/200617_4b2je2aibcd4eacdb65kk4e690737_750x1125.jpg",
                    "title": "蕾丝连衣裙女夏季新款法式气质显瘦中长款超仙小个子收腰网纱裙子",
                    "price": 88.2,
                    "collection": 247
                },
                {
                    "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1mjdsek&acm=3.ms.1_4_1mjdsek.46.36613-93872-68998.dQSxjs2fTg747.sd_117-swt_46-imt_6-c_1_17_514533610_0_0_3-t_mLA6Hs2fSXRlg-lc_17-pit_1-qid_90128-dit_&cparam=MTU5MjQ3MzY3N18xMWtfNmJiMDI5MjE2ZGVjODVhMDUzYjJmMzcyZjk1YTc4NTNfMTdfMF81MTQ1MzM2MTBfNGY4Zl8wXzBfMF8zMF8xXzNfbG9jLTA=",
                    "image": "https://s5.mogucdn.com/mlcdn/776a41/200617_1d143cj0ia5c4k86c4kggl1if4g1e_750x1125.jpg",
                    "title": "2020新款V领连衣裙女气质显瘦收腰赫本风小黑裙夏黑色裙子潮",
                    "price": 58.5,
                    "collection": 190
                },
                {
                    "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1mt78ju&acm=3.ms.1_4_1mt78ju.46.36613-93872-68998.dQSxjs2fTg747.sd_117-swt_46-imt_6-c_1_17_574775867_0_0_3-t_mLA6Hs2fSXRlg-lc_17-pit_1-qid_90128-dit_&cparam=MTU5MjQ3MzY3N18xMWtfNmJiMDI5MjE2ZGVjODVhMDUzYjJmMzcyZjk1YTc4NTNfMTdfMF81NzQ3NzU4NjdfNGNfMF8wXzBfMjQzXzFfM19sb2MtMA==",
                    "image": "https://s5.mogucdn.com/mlcdn/776a41/200617_509lbb1ahf9i9c9cja0i6aak07b46_750x1125.jpg",
                    "title": "夏季新款气质收腰显瘦小个子裙子设计感假两件撞色拼接连衣裙女",
                    "price": 69,
                    "collection": 413
                },
                {
                    "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1mezp2w&acm=3.ms.1_4_1mezp2w.46.36613-93872-68998.dQSxjs2fTg747.sd_117-swt_46-imt_6-c_1_17_489959124_0_0_3-t_mLA6Hs2fSXRlg-lc_17-pit_1-qid_90128-dit_&cparam=MTU5MjQ3MzY3N18xMWtfNmJiMDI5MjE2ZGVjODVhMDUzYjJmMzcyZjk1YTc4NTNfMTdfMF80ODk5NTkxMjRfNGY4YV8wXzBfMF81NzVfMV8zX2xvYy0w",
                    "image": "https://s5.mogucdn.com/mlcdn/776a41/200617_1flf55379bag200573115589l4ajg_750x1125.jpg",
                    "title": "套装宽松显瘦微胖减龄藏肉连衣裙中长款简约T恤+A字牛仔短裙",
                    "price": 44.99,
                    "collection": 14821
                },
                {
                    "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1mt9xe4&acm=3.ms.1_4_1mt9xe4.46.36613-93872-68998.dQSxjs2fTg747.sd_117-swt_46-imt_6-c_1_17_574775789_0_0_3-t_mLA6Hs2fSXRlg-lc_17-pit_1-qid_90128-dit_&cparam=MTU5MjQ3MzY3N18xMWtfNmJiMDI5MjE2ZGVjODVhMDUzYjJmMzcyZjk1YTc4NTNfMTdfMF81NzQ3NzU3ODlfNGNfMF8wXzBfMjQzXzFfM19sb2MtMA==",
                    "image": "https://s5.mogucdn.com/mlcdn/776a41/200617_1j0lhc39k8jl15jlac54h39k597e8_750x1125.jpg",
                    "title": "胖mm洋气减龄遮肚子显瘦连衣裙女夏季新款网纱拼接小个子裙子",
                    "price": 79,
                    "collection": 349
                },
                {
                    "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1mef2fi&acm=3.ms.1_1_1mef2fi.46.67824-68998.dQSxjs2fTg747.ct_3100-sd_117-swt_46-imt_7-c_2_17_485329116_2081815_40_0-t_mLA6Hs2fSXRlg-lc_17-pit_2-c1_88933_nil_nil_0_2081815_30_0-dit_&cparam=MTU5MjQ3MzY3N18xMWtfNmJiMDI5MjE2ZGVjODVhMDUzYjJmMzcyZjk1YTc4NTNfMTdfOV80ODUzMjkxMTZfNGU4Zl8yMDgxODE1XzQwXzBfMTgwXzFfMF9ycy04ODkzMy5ydC0xLnd0LTE=",
                    "image": "https://s5.mogucdn.com/mlcdn/17f85e/190309_293979890ibgf0kf45c3hh3i8e21a_640x960.jpg",
                    "title": "2019春夏装新款时尚套装新品女士时尚运动套装休闲九分裤套装韩大码女装两件套",
                    "price": 89,
                    "collection": 171
                },
                {
                    "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1mtqffs&acm=3.ms.1_1_1mtqffs.46.67824-68998.dQSxjs2fTg747.ct_3100-sd_117-swt_46-imt_7-c_2_17_576933329_548773411_39_0-t_mLA6Hs2fSXRlg-lc_17-pit_2-c1_88933_nil_nil_1_548773411_30_0-dit_&cparam=MTU5MjQ3MzY3N18xZzF3a3E4XzZmOTU0ODQ4ZmIzOWY2MjgyMTYwYzA1ZDkzNWNlNmEwXzE3XzhfNTc2OTMzMzI5XzRmODZfMF8zOV8wXzEyMF8xXzBfcnMtODg5MzMucnQtMS53dC0x",
                    "image": "https://s5.mogucdn.com/mlcdn/c45406/200601_6k432748f5e0gcidg0c9dc1f5e41k_3999x5999.jpg",
                    "title": "2020夏季新款女装韩版时尚九分裤小个子两件套休闲洋气套装",
                    "price": 61.6,
                    "collection": 39
                },
                {
                    "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1mt3ity&acm=3.ms.1_4_1mt3ity.46.36613-93872-68998.dQSxjs2fTg747.sd_117-swt_46-imt_6-c_1_17_573835316_0_0_3-t_mLA6Hs2fSXRlg-lc_17-pit_1-qid_90128-dit_&cparam=MTU5MjQ3MzY3N18xMWtfNmJiMDI5MjE2ZGVjODVhMDUzYjJmMzcyZjk1YTc4NTNfMTdfMF81NzM4MzUzMTZfNGNfMF8wXzBfODIzXzFfM19sb2MtMA==",
                    "image": "https://s5.mogucdn.com/mlcdn/776a41/200617_2lceddda13kel8c90cg49gh04613d_750x1125.jpg",
                    "title": "夏季新款v领仙女裙chic温柔小个子短袖雪纺短裙子白色连衣裙",
                    "price": 88,
                    "collection": 426
                },
                {
                    "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1mrcl4y&acm=3.ms.1_4_1mrcl4y.46.36613-93872-68998.dQSxjs2fTg747.sd_117-swt_46-imt_6-c_1_17_561213398_0_0_3-t_mLA6Hs2fSXRlg-lc_17-pit_1-qid_90128-dit_&cparam=MTU5MjQ3MzY3N18xMWtfNmJiMDI5MjE2ZGVjODVhMDUzYjJmMzcyZjk1YTc4NTNfMTdfMF81NjEyMTMzOThfNGY4ZF8wXzBfMF81ODFfMV8zX2xvYy0w",
                    "image": "https://s5.mogucdn.com/mlcdn/776a41/200617_2ebcd32593geigj41j82fb32f6lfl_750x1125.jpg",
                    "title": "夏季韩版宽松五分袖卡通T恤高腰牛仔阔腿短裤子时尚套装两件套女",
                    "price": 39.6,
                    "collection": 249
                },
                {
                    "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1mt3hy4&acm=3.ms.1_4_1mt3hy4.46.36613-93872-68998.dQSxjs2fTg747.sd_117-swt_46-imt_6-c_1_17_573835310_0_0_3-t_mLA6Hs2fSXRlg-lc_17-pit_1-qid_90128-dit_&cparam=MTU5MjQ3MzY3N18xMWtfNmJiMDI5MjE2ZGVjODVhMDUzYjJmMzcyZjk1YTc4NTNfMTdfMF81NzM4MzUzMTBfNGNfMF8wXzBfODIzXzFfM19sb2MtMA==",
                    "image": "https://s5.mogucdn.com/mlcdn/776a41/200617_44fa567j52g7bfd4c3303027c7bfj_750x1125.jpg",
                    "title": "夏季新款韩版中长款收腰显瘦喇叭袖小清新裙子碎花雪纺连衣裙女",
                    "price": 71,
                    "collection": 616
                },
                {
                    "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1msctwm&acm=3.ms.1_4_1msctwm.46.36613-93872-68998.dQSxjs2fTg747.sd_117-swt_46-imt_6-c_1_17_568504384_0_0_3-t_mLA6Hs2fSXRlg-lc_17-pit_1-qid_90128-dit_&cparam=MTU5MjQ3MzY3N18xMWtfNmJiMDI5MjE2ZGVjODVhMDUzYjJmMzcyZjk1YTc4NTNfMTdfMF81Njg1MDQzODRfNGY4ZF8wXzBfMF8yMzRfMV8zX2xvYy0w",
                    "image": "https://s5.mogucdn.com/mlcdn/776a41/200617_4ddi8b66ldl48be84dl6h75f0b4g1_750x1125.jpg",
                    "title": "夏季新款嘻哈风印花短袖T恤+束脚拼接运动休闲裤时尚套装两件套",
                    "price": 44.1,
                    "collection": 482
                },
                {
                    "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1medwhg&acm=3.ms.1_4_1medwhg.46.36613-93872-68998.dQSxjs2fTg747.sd_117-swt_46-imt_6-c_1_17_486801840_0_0_3-t_mLA6Hs2fSXRlg-lc_17-pit_1-qid_90128-dit_&cparam=MTU5MjQ3MzY3N18xMWtfNmJiMDI5MjE2ZGVjODVhMDUzYjJmMzcyZjk1YTc4NTNfMTdfMF80ODY4MDE4NDBfNGNfMF8wXzBfMjM0XzFfM19sb2MtMA==",
                    "image": "https://s5.mogucdn.com/mlcdn/776a41/200617_6fkag66f6c46ei707l7k0j174l9d9_750x1125.jpg",
                    "title": "春夏宽松学生休闲运动服套装女时尚韩版连帽上衣+九分裤两件套潮",
                    "price": 44.9,
                    "collection": 8632
                },
                {
                    "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1mrxe1o&acm=3.ms.1_4_1mrxe1o.46.36613-93872-68998.dQSxjs2fTg747.sd_117-swt_46-imt_6-c_1_17_565503576_0_0_3-t_mLA6Hs2fSXRlg-lc_17-pit_1-qid_90128-dit_&cparam=MTU5MjQ3MzY3N18xMWtfNmJiMDI5MjE2ZGVjODVhMDUzYjJmMzcyZjk1YTc4NTNfMTdfMF81NjU1MDM1NzZfNGNfMF8wXzBfMTk0XzFfM19sb2MtMA==",
                    "image": "https://s5.mogucdn.com/mlcdn/776a41/200617_5lkilka6jh8cgl0lb29deflkaf934_750x1125.jpg",
                    "title": "小心机设计感V领泡泡袖针织T恤+收腰碎花半身裙甜美两件套装女",
                    "price": 35.6,
                    "collection": 1003
                },
                {
                    "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1mtwiba&acm=3.ms.1_1_1mtwiba.46.67824-68998.dQSxjs2fTg747.ct_3100-sd_117-swt_46-imt_7-c_2_17_577741571_549343294_38_0-t_mLA6Hs2fSXRlg-lc_17-pit_2-c1_88933_nil_nil_1_549343294_30_0-dit_&cparam=MTU5MjQ3MzY3N18xajJ6ZDk2XzE3MjkzODJkOWZiNDM4ZDJmYWYxYTY2OGM5ZTFhODliXzE3XzdfNTc3NzQxNTcxXzRlOGZfMF8zOF8wXzQwXzFfMF9ycy04ODkzMy5ydC0xLnd0LTA=",
                    "image": "https://s5.mogucdn.com/mlcdn/c45406/200607_28la61b3f0haeih23hc8291lb0d3j_3999x5999.jpg",
                    "title": "2020新款女装夏两件套裤短袖t恤雪纺+阔脚裤休闲时尚套装女",
                    "price": 72.16,
                    "collection": 27
                },
                {
                    "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1mtptru&acm=3.ms.1_1_1mtptru.46.67824-68998.dQSxjs2fTg747.ct_3100-sd_117-swt_46-imt_7-c_2_17_576626522_548622911_37_0-t_mLA6Hs2fSXRlg-lc_17-pit_2-c1_88933_nil_nil_1_548622911_30_0-dit_&cparam=MTU5MjQ3MzY3N18xajN5MGppX2MxNWQ4ZGU4M2U3MjU5MjQ4MmMxM2JhNTEzNjdmNzFjXzE3XzZfNTc2NjI2NTIyXzRmODZfMF8zN18wXzc5XzFfMF9ycy04ODkzMy5ydC0xLnd0LTA=",
                    "image": "https://s5.mogucdn.com/mlcdn/c45406/200530_66ed509aji00iceb61flla52aidg6_3999x5999.jpg",
                    "title": "大码女装夏新款休闲气质收腰显瘦连衣裙性感V领洋气遮肉裙子",
                    "price": 130.53,
                    "collection": 23
                },
                {
                    "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1msvedi&acm=3.ms.1_4_1msvedi.46.36613-93872-68998.dQSxjs2fTg747.sd_117-swt_46-imt_6-c_1_17_573299980_0_0_3-t_mLA6Hs2fSXRlg-lc_17-pit_1-qid_90128-dit_&cparam=MTU5MjQ3MzY3N18xMWtfNmJiMDI5MjE2ZGVjODVhMDUzYjJmMzcyZjk1YTc4NTNfMTdfMF81NzMyOTk5ODBfNDhfMF8wXzBfNzU5XzFfM19sb2MtMA==",
                    "image": "https://s5.mogucdn.com/mlcdn/776a41/200617_669k9g4f17l70h6912jiiiklh42e0_750x1125.jpg",
                    "title": "连衣裙女夏气质小个子搭配显瘦显高收腰矮个子衬衫短裤时尚套装裙",
                    "price": 76.5,
                    "collection": 176
                },
                {
                    "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1mt5wcq&acm=3.ms.1_4_1mt5wcq.46.36613-93872-68998.dQSxjs2fTg747.sd_117-swt_46-imt_6-c_1_17_574009681_0_0_3-t_mLA6Hs2fSXRlg-lc_17-pit_1-qid_90128-dit_&cparam=MTU5MjQ3MzY3N18xMWtfNmJiMDI5MjE2ZGVjODVhMDUzYjJmMzcyZjk1YTc4NTNfMTdfMF81NzQwMDk2ODFfNGNfMF8wXzBfMTE0XzFfM19sb2MtMA==",
                    "image": "https://s5.mogucdn.com/mlcdn/776a41/200617_1j5ddia552dkakce5l0hg49ac6l17_750x1125.jpg",
                    "title": "小个子可甜可盐连衣裙收腰显瘦气质法式雪纺裙+打底短裤",
                    "price": 20.7,
                    "collection": 169
                },
                {
                    "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1m4e1a8&acm=3.ms.1_4_1m4e1a8.46.36613-93872-68998.dQSxjs2fTg747.sd_117-swt_46-imt_6-c_1_17_405038066_0_0_3-t_mLA6Hs2fSXRlg-lc_17-pit_1-qid_90128-dit_&cparam=MTU5MjQ3MzY3N18xMWtfNmJiMDI5MjE2ZGVjODVhMDUzYjJmMzcyZjk1YTc4NTNfMTdfMF80MDUwMzgwNjZfNDhfMF8wXzBfNDQ3XzFfM19sb2MtMA==",
                    "image": "https://s5.mogucdn.com/mlcdn/776a41/200617_4agc9dij77k60fbjl5bd4je1c41ia_750x1125.jpg",
                    "title": "系带蝴蝶结少女心红色格子连衣裙女夏季新款韩版V领修身显瘦A字裙子仙",
                    "price": 73.8,
                    "collection": 18101
                },
                {
                    "link": "https://h5.mogu.com/detail-normal/index.html?itemId=1msfhcs&acm=3.ms.1_4_1msfhcs.46.36613-93872-68998.dQSxjs2fTg747.sd_117-swt_46-imt_6-c_1_17_568899208_0_0_3-t_mLA6Hs2fSXRlg-lc_17-pit_1-qid_90128-dit_&cparam=MTU5MjQ3MzY3N18xMWtfNmJiMDI5MjE2ZGVjODVhMDUzYjJmMzcyZjk1YTc4NTNfMTdfMF81Njg4OTkyMDhfNGNfMF8wXzBfMTI2XzFfM19sb2MtMA==",
                    "image": "https://s5.mogucdn.com/mlcdn/776a41/200617_537je9g6e69486ike4d0f0g0k8g18_750x1125.jpg",
                    "title": "夏季新款小个子灯笼袖蕾丝衬衫+显瘦牛仔半身裙时尚套装两件套",
                    "price": 44.1,
                    "collection": 1058
                }
            ],
            "pageInfo": {
                "allCount": 80,
                "page": 1,
                "pageSize": 20
            }
        }
    }
