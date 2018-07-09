#!user/bin/python
# encoding:utf-8
import requests
import json
import time

url = 'http://order.mi.com/login/callback'
query_args = {
    "usr": "13148817544",
    "tsl": "1",
    "sign": "NWU4MzRmNjBhZmU4MDRmNmZkYzVjMTZhMGVlMGFmMTllMGY0ZTNhZQ,,",
    "pwd": "1",
    "pass_uas": "1.0",
    "pass_ss": "4.0",
    "pass_eas": "2.0",
    "nonce": "/40ucOGde1MBdTzW",
    "m": "3",
    "followup": "http://www.mi.com/",
    "d": "wb_9a67ef7a-379b-40a1-8092-5bd20e486fe3",
    "auth": "iwdgM0J1BMElo84TcZaTEjWUJEe+HrtxcB08/5M/yC0Hx43ffLnoMl6fu1Kq/kSEy5j49DIF/srTkTVsDYuMA8A+28pAthzQIgyTCtZTRU0lDmswquwCEhnR7pv5Mck2Kn2syb0xhV9DvNph+45l88KAXW0YbHJ0VPDsjSTHp+s=",
    "_ssign": "otx2si5SNSqZnxgLh6ojKQFv58o="
}
head = dict()
head['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
head['Accept-Encoding'] = 'gzip, deflate, sdch'
head['Accept-Language'] = 'zh-CN,zh;q=0.8'
head[
    'User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                    'Chrome/45.0.2454.101 Safari/537.36'

s = requests.Session()
s.headers.update(head)
r = s.get(url, data=query_args)
print r

url = "http://a.stat.xiaomi.com/js/mstr.js"
query_args = {
    "mstpid": "手机版本选择页面_立即购买",
    "mid": "75210645",
    "phpsessid": "",
    "sessionId": "442449448",
    "muuid": "1467629390692_2635",
    "mucid": "",
    "pass_eas": "2.0",
    "mstprevpid": u"手机版本选择页面_立即购买",
    "timestamp": time.time(),  # "1467718763141"
    "domain": ".mi.com",
    "screen": "1440*900",
    "language": "zh-cn",
    "vendor": "undefined",
    "target": "Win32",
    "platform": "mi5_2160700016",
    "prevtarget": "mi5_2160700016",
    "pid_loc": "pcpid",
    "mstprev_pid_loc": "pcpid",
    "mstprev_pid_loc": "pcpid",
    "domain_id": "100",
    "pageid": "9899b068fcb38b0e",
    "curl": "http://item.mi.com/buyphone/mi5",
    "xmv": "1467715788702_742_1467718411931",
    "v": "GCO0CUMIGV5OEDAS",
}
head = dict()
head['Accept'] = '*/*'
head['Accept-Encoding'] = 'gzip, deflate'
head['Accept-Language'] = 'zh-CN'
head[
    'User-Agent'] = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;' \
                    ' .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E; InfoPath.3)'
s.headers.update(head)
r = s.get(url, data=query_args)
print r
