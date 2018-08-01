# coding:utf-8
# !/user/bin/python
from celery import Celery

app = Celery('hello', broker='redis://localhost:6379/1')


@app.task
def hello():
    return 'hello world'


@app.task
def add(a, b):
    return a + b
