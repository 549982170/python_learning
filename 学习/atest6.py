# coding:utf-8
# !/user/bin/python
import requests
import json

headers = {'Authorization': "Token 03f7409574a55e98cd33b7cc44bcbe968fd0988f"}
host = "http://127.0.0.1:8000/"

url = "v5/discovery/search/service/"
# url = "v1/generator/test/mytest/"
url = host + url
data = {"keyword": "ss"}
re = requests.post(url)
re = requests.post(url, data=data, headers=headers)
print re.text
#
# a = "ssddda"
# print a[-1:]
