#!/usr/bin/env python
#coding=utf-8
import os
import sys

root = os.path.dirname(__file__)

sys.path.insert(0, os.path.join(root, 'site-packages'))

import sae


import django
'''
from yzwBlog import wsgi

application=sae.create_wsgi_app(wsgi.application)
'''
def application(environ, start_response):
    start_response('200 ok', [('content-type', 'text/plain')])
    s=str(django.VERSION)
    return s