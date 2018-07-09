# encoding:utf-8
# usr/bin/python
import requests
import ssl

url = "https://10fastfingers.com/speedtests/get_words"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Accept-Encoding': 'gzip',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Host': 'q.115.com',
    'Connection': 'Keep-Alive',
    'Cookie': 'CakeCookie[lang]=Q2FrZQ%3D%3D.304a; CakeCookie[alternate_language_suggestion]=Q2FrZQ%3D%3D.zlIIRA%3D%3D; _fssid=6ebf573e-25e5-4ebd-ac0e-a32a051129c6; __qca=P0-1973442476-1510797527014; _fsuid=58d51934-72c2-4896-ba65-a2285427096f; _dm_sync=true; _dm_bid=true; CAKEPHP=031s2f2ch5fer22a5i64b1ubr3; __utma=129363724.1488205825.1510797526.1510797526.1510797526.1; __utmb=129363724.23.9.1510797572271; __utmc=129363724; __utmz=129363724.1510797526.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'
}

s = requests.Session()
s.headers.update(headers)

# result = s.post(url, verify=False)
# print result.text

import urllib3
from urllib3.contrib.appengine import AppEngineManager
import certifi
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
result = http.request('POST', url)
print result
