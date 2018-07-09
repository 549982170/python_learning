# coding:utf8
import json
from dbpool import DBPool
config = json.load(open('config.json', 'r'))
adminPool = DBPool()
adminPool.initPool(config['admin'])
sql = "select * from post"
print adminPool.querySql(sql)