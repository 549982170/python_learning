#!/usr/bin/python
# coding: UTF-8
a = {"test1": 1, "test2": 2, "test3": 3, "test4": 4, "test5": 5, "test6": 6}

# for c in  a.values():
#     print c
import logging
# 创建一个logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)
# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('a.log')
fh.setLevel(logging.DEBUG)
# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# 定义handler的输出格式
formatter = logging.Formatter()
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# 给logger添加handler
logger.addHandler(fh)
logger.addHandler(ch)
try:
    raise Exception(u'中')
except Exception as e:
    logger.error(e)