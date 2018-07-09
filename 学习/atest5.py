# coding:utf-8
# !/user/bin/python
import requests

url = "http://d-api.soovii.com:6565/api/getProjectInfoAPI"
r = requests.post(url)
print r.json()
