# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

from Yiche import settings

# 将数据存储到MongoDB数据库中
class YichePipeline(object):
    def __init__(self):
        host = settings['HOST']
        port = settings['PORT']
        dbnam = settings['DBNAME']
        dbtable = settings['DBNAME_TABLE']
        client = pymongo.MongoClient(host=host,port=port)
        db = client[dbnam]
        self.post = db[dbtable]
    def process_item(self, item, spider):
        item = dict(item)
        self.post.insert(item)
        return item



