# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhiyoujiItem(scrapy.Item):
    # define the fields for your item here like:
    # 公司名称
    name = scrapy.Field()
    # 浏览量
    browse = scrapy.Field()
    # 公司信息
    message = scrapy.Field()
    # 公司行业
    industry = scrapy.Field()
    # 公司简称
    abb = scrapy.Field()
    # 公司概述
    summ = scrapy.Field()
    # 好评度
    dop = scrapy.Field()
    # 薪资
    pay = scrapy.Field()
    # 产品
    product = scrapy.Field()
    # 融资情况
    financing = scrapy.Field()
    # 排名
    ranking = scrapy.Field()
    # 地址
    add = scrapy.Field()
    # 网址
    web = scrapy.Field()
    # 联系方式
    tel = scrapy.Field()
    # QQ
    qq = scrapy.Field()
    pass
