#coding=utf-8
import requests
url = 'http://localhost:8080'
path = u'F://123//1.gif'
print path
files = {'file': open(path, 'rb')}
r = requests.post(url, files=files)
print r.url,r.text