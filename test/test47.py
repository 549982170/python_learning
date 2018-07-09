#!/usr/bin/env python
# encoding:utf8
import os
for root, dirs, files in os.walk('./'):
    print root, dirs, files
    break


def composed(*decs):
    def deco(f):
        for dec in reversed(decs):
            f = dec(f)
        return f
    return deco

@composed(dec1, dec2)
def some(f):
    pass

@multiple_decorators
def foo(): pass

def multiple_decorators(func):
   return decorator1(decorator2(func))

@multiple_decorators
def foo(): pass

def compose(f, g):
    return lambda x: f(g(x))

combined_decorator = compose(decorator1, decorator2)

@combined_decorator
def f():
    pass


@mod.route('/standardization/<sid>')
@login_required
def scriptstandardization(sid):
    pass


from flask_login import login_required

def needloginroute(f,url, g=login_required):
    return lambda x: f.route(url)(g(x))

@needloginroute(mod, '/standardization/<sid>')
def scriptstandardization(sid):
    pass

from flask import  Blueprint
mod = Blueprint('script', __name__)

def compose(f, g):
    return lambda x: f('f的参数')(g('g的参数')(x))

def myroute(f,url, g=login_required, needlogin=True,**kwargs):
    """必须登录的装饰器
    @parma f:蓝图的mod
    @parma url:路由url
    @parma g:login_required装饰器
    @param needlogin: True时为需要登录(默认)
    """
    if needlogin:
        return lambda x: f.route(url,**kwargs)(g(x))
    else:
        return lambda x: f.route(url,**kwargs)(x)