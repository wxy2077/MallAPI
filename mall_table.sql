-- Mysql 数据库 建表语句 以及部分数据



-- 首页数据库轮播图banner
CREATE TABLE `mall_banner` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `link` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '链接地址',
  `image` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '轮播图',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;



-- 商品分类表
CREATE TABLE `mall_goods_cate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cate_id` int(11) DEFAULT NULL COMMENT '分类id',
  `cate_name` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '分类名称',
  `cate_thumbnail` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '分类缩略图',
  PRIMARY KEY (`id`),
  UNIQUE KEY `c_uk` (`cate_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;



-- 商品表 mall_goods
CREATE TABLE `mall_goods` (
  `goods_id` int(11) NOT NULL AUTO_INCREMENT,
  `link` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '链接地址',
  `image` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '图片',
  `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '标题',
  `describe` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '描述',
  `cate_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '分类id',
  `tab_id` int(64) DEFAULT NULL COMMENT '一对多tab',
  `is_features` smallint(2) DEFAULT NULL COMMENT '是否特色(首页推荐)',
  `features_image` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '推荐缩略图',
  `is_recommends` smallint(2) DEFAULT NULL COMMENT '是否推荐',
  `price` float DEFAULT NULL COMMENT '价格',
  `collection` int(64) DEFAULT NULL COMMENT '收藏数',
  `thumbnail` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '缩略图',
  PRIMARY KEY (`goods_id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


-- 商品标签表
CREATE TABLE `mall_tab` (
  `tab_id` int(11) NOT NULL AUTO_INCREMENT,
  `is_home` smallint(2) DEFAULT NULL COMMENT '是否首页展示',
  `tab_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '标签名称',
  `cate_id` int(11) DEFAULT NULL COMMENT '对应分类标签',
  PRIMARY KEY (`tab_id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;





-- 商品(goods)对应多个标签(tab)中间表 （暂时没用这张表 一个商品 多个tab）
CREATE TABLE `mall_goods_to_tab` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `goods_id` int(11) DEFAULT NULL COMMENT '商品id',
  `tab_id` int(11) DEFAULT NULL COMMENT 'tab标签id',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_g_t` (`goods_id`,`tab_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


-- 商品详情表 mall_goods_detail
CREATE TABLE `mall_goods_detail` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '唯一键',
  `goods_id` int(11) DEFAULT NULL COMMENT '商品id',
  `banners` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci COMMENT '轮播图list 用,隔开',
  `title` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '标题',
  `price` decimal(10,2) DEFAULT NULL COMMENT '价格',
  `original_price` decimal(10,2) DEFAULT NULL COMMENT '原价',
  `sales_volume` int(11) DEFAULT NULL COMMENT '销量',
  `sales_collect` int(11) DEFAULT NULL COMMENT '收藏数量',
  `sales_deliver` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '发货时间',
  `discount_volume` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '折扣券(满99减2)用,隔开',
  `discount_activity` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '折扣活动(买两件送一件)用,隔开',
  `logistics_info` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '物流信息 用,隔开',
  `shop_id` int(11) DEFAULT NULL COMMENT '商家信息',
  `goods_image` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci COMMENT '商品图片信息存list 用,隔开',
  `goods_desc` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '商品描述',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;




-- select goods_id, banners, title, price, original_price, sales_volume, sales_collect,
-- sales_deliver, discount_volume, discount_activity, logistics_info, shop_id, goods_image, goods_desc from mall_goods_detail where goods_id=123

-- 店铺表 mall_shop
CREATE TABLE `mall_shop` (
  `shop_id` int(11) NOT NULL,
  `shop_name` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '店铺名称',
  `shop_image` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '店铺头像',
  `credit_rating` varchar(255) COLLATE utf8mb4_general_ci NOT NULL COMMENT '信用级别',
  `goods_num` int(11) DEFAULT NULL COMMENT '商品数量(正规应该查询)',
  `follow` int(11) DEFAULT NULL COMMENT '关注数',
  `cumulative_sales` int(255) DEFAULT NULL COMMENT '累计销量',
  PRIMARY KEY (`shop_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;



-- select shop_name, shop_image,credit_rating, goods_num, follow, cumulative_sales from mall_shop
-- where shop_id=2001

-- 商品评论表 mall_goods_comment
CREATE TABLE `mall_goods_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '唯一id',
  `goods_id` int(11) NOT NULL COMMENT '评论商品id',
  `user_id` int(11) DEFAULT NULL COMMENT '用户id',
  `comment` varchar(255) DEFAULT NULL COMMENT '评论信息',
  `buy_info` varchar(255) DEFAULT NULL COMMENT '购买商品信息',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- select user_id, comment, buy_info from mall_goods_comment where goods_id=123 order id desc limit 2





