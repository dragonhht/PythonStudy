#! /usr/bin/python
# coding: utf-8

"""
连接Mongodb,基本的增删改查操作
"""

from pymongo import MongoClient
import datetime
# 连接信息 mongodb://${user}:${password}@${host}:${port}
host = 'mongodb://root:123@my.dragon.com:27017'

client = MongoClient(host)
# 连接test数据库
db = client.test
# 选择blog集合
collection = db.blog

data = {"name": "dragonhht", "date": datetime.datetime.utcnow()}
# 保存数据
collection.save(data)

# 查找
for result in collection.find():
    print(result)
print(collection.find_one({"name" : "dragonhht"}))

# 更新, 更新name为dragonhht的记录，将时间进行更新
collection.update({"name" : "dragonhht"}, {"$set" : {"date" : datetime.datetime.utcnow()}})

# 删除
#collection.remove({"name" : "dragonhht"})