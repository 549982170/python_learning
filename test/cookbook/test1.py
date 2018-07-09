#!/usr/bin/python
# coding: UTF-8
from flask import Flask

app = Flask(__name__)
print "test"
if __name__ == "__main__":
    app.debug = True  # DEBUG模式下flask开多一个线程来监视项目的变化
    app.run(use_reloader=False)
