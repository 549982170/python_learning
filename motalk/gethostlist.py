#-*- coding:utf-8 -*-
import json
import requests



r = requests.get('http://www.moxiancn.com/mo_talk/m1/gethostlist')

print r.json()
