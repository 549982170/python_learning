__author__ = 'blue'
#coding:utf-8

import requests
import json
import time
import hashlib



proxies = {
    # 'http': 'http://127.0.0.1:8888',
}

headers = {
            'User-Agent': 'Mozilla/5.0 (HUAWEIU9508; 4.2.2; zh;) 115disk/5.5.5',
            'Accept-Encoding': 'gzip',
            'Content-Type': 'application/x-www-form-urlencoded',
            # 'Host': 'q.115.com',
            'Connection': 'Keep-Alive',
            'Cookie':'__cfduid=d929fe0dddbaca961f4391ca7a1d1af891418023020; CNZZDATA620725=cnzz_eid%3D495694148-1423209010-%26ntime%3D1423213313; __auc=71651c2414a5d131de56c08eee2; PHPSESSID=dsu0lp7r9h1hogajtpagknqqm4; PHPSESSID=cnh2umanrsrdbpb4ul63nbeku7; __utma=41008823.1916397147.1415083690.1425975089.1433213508.60; __utmc=41008823; __utmz=41008823.1415083690.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); hl=zh-cn; __utmt=1; __utma=94681600.586131560.1415082849.1433225605.1433237664.246; __utmb=94681600.62.10.1433237664; __utmc=94681600; __utmz=94681600.1433237664.246.104.utmcsr=debug.moxian.com|utmccn=(referral)|utmcmd=referral|utmcct=/; a2404_pages=314; a2404_times=3; mx_lang=cs'
        }


url1 = "http://data.debug.moxian.com/import2user/Ajaxunupdate"
url2 = "http://data.debug.moxian.com/import2user/ajaxsync"


while True:
    r  = requests.get(url=url1,headers=headers,proxies=proxies)
    res = r.json()
    data = res.get("data",{})
    total = data.get("total",0)
    idlist = data.get("list",'')
    # print idlist
    # exit()
    if total==0:
        break
    payload    = {
        'pwd'         : 'moxian@10086mx',
        'ids'         : idlist,
    }

    r = requests.post(url2, data=payload, headers=headers,proxies=proxies)
    print r.json()

print 'over'

# print r.text
# print r.content
# print r.url
# print r.encoding
# print type(r.status_code )                   # response status code(eg:200)
# print r.headers                        # a dict
# print r.headers['Content-Type']        # response headers
#print r.cookies['example_cookie_name'] # cookies
                        #  built-in json function

# print r.request.headers         # http request headers