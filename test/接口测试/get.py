#!/usr/bin/env python
# encoding:utf8
import requests
import json

url = 'http://127.0.0.1:8080/userver/game/getSvrList'
payload = {"channelId": 1015, "installId": "1.9.8", "mac": "D6EF5F90-56AE-4B5A-A5B7-E993EFB08976"}

r = requests.post(url, params)
print r.text
