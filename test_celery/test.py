# coding:utf-8
# !/user/bin/python
from test_celery.tasks import add

print add.delay(1,2)
