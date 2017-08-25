# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhilianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 招聘名称
    name = scrapy.Field()
    # 招聘单位
    company = scrapy.Field()
    # 发布时间
    time = scrapy.Field()
    # 薪资
    pay = scrapy.Field()
    # 工作地点
    rddress = scrapy.Field()
    # 工作经验
    experience = scrapy.Field()
    # 学历要求
    degree = scrapy.Field()
    # 招聘人数
    number = scrapy.Field()
    # 职位类别
    sort = scrapy.Field()
    # 职位描述
    describe = scrapy.Field()
    # 公司介绍
    #introduce = scrapy.Field()
    # 工作地点
    work_rdd = scrapy.Field()
    pass
