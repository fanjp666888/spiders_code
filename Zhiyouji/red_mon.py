# 将redis中的数据存储到mongodb数据库中
import redis
from pymongo import MongoClient
import json

def redmon():
    # 1.链接redis数据库
    redis_cli = redis.Redis('192.168.133.101','6379',0)
    # 2.链接mongodb数据库并建数据库和集合
    print("@@@@@@@@@@")
    mongodb_cli = MongoClient('127.0.0.1:27017')
    db = mongodb_cli['ZhiYou']
    col =db['zhiyou']
    print("#############")
    # 3.将redis中的数据导出再导入mongodb中
    while True:
        scores,data = redis_cli.blpop(["zhiyouji:items"])
        print(data)
        item = json.loads(data.decode())
        col.insert(item)
if __name__ == '__main__':
    redmon()