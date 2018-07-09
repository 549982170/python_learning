#!/usr/bin/python3
# coding: UTF-8
from util import querySql, logger

sql = "select * from pm_attendance_record"
result = querySql(sql, True)
logger.info("start")
for ca in result:
    logger.info(ca)
logger.info("end")
print("finish")
