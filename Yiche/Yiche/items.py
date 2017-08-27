# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YicheItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 品牌
    series = scrapy.Field()
    # 车型
    car = scrapy.Field()
    # 参考价
    reference = scrapy.Field()
    # 排量
    #displacement = scrapy.Field()
    # 关注度
    #attention = scrapy.Field()
    # 变速箱
    #gearbox = scrapy.Field()
    # 指导价
    #guidance = scrapy.Field()
    # 最低价
    #minimum = scrapy.Field()
    # 车辆各配置信息
    info  = scrapy.Field()
    # 口碑评分
    graded = scrapy.Field()
    pass
