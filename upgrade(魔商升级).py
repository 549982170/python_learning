__author__ = 'blue'
#coding:utf-8

import requests
import json
import time
import hashlib

config_env = 'yxhk'

mx_id          = "283966" # mx_id
shop_id        = "CNM8751567" # shop_id
level          = "1"
unix_timestamp = str(int(time.time()))

key = 'ual%$Fi1230+=update99*tM||#'
secret_answer = hashlib.md5(hashlib.md5(mx_id + "|" +shop_id + "|" + unix_timestamp + "|" + key).hexdigest()).hexdigest()

payload    = {
    'level'         : level,
    'mx_id'         : mx_id,
    'shop_id'       : shop_id,
    'unix_timestamp': unix_timestamp,
    'secret_answer' : secret_answer,
}

headers    = {'content-type': 'application/x-www-form-urlencoded'}
proxies = {
    # 'http' : 'http://127.0.0.1:8888',
}
url = {
    'm1'   : "http://m1.moxian.com/merchant/api/upgradlevel",
    'dev'  : "http://dev.moxian.com/merchant/api/upgradlevel",
    'debug': "http://debug.moxian.com/merchant/api/upgradlevel",
    'yxhk' : "http://yxhk.moxian.com/merchant/api/upgradlevel",
    'ml'   : "http://moxian.com/merchant/api/upgradlevel",
}



r = requests.post(url[config_env], data=payload, headers=headers,proxies=proxies)

# print r.text
# print r.content
# print r.url
# print r.encoding
# print r.status_code                    # response status code(eg:200)
# print r.headers                        # a dict
# print r.headers['Content-Type']        # response headers
#print r.cookies['example_cookie_name'] # cookies
print r.json()                         #  built-in json function

# print r.request.headers         # http request headers