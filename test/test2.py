# encoding:utf-8
# a = "132, 176 | 504, 624 | 1154, 1421 | 3754, 4621 | 7360, 9126 | 13610, 16876 | 26110, 32376 | 51110, 63376"
# print len(a.split('|'))
# import datetime, time
#
# t_str = '20131130 20:44'
# d = datetime.datetime.strptime(t_str, '%Y%m%d %H:%M')
# print time.time()-10000

from collections import OrderedDict


# s = "[{10002:[11,22]},{10001:[11,22]},{10003:[11,22]}]"
#
# b = eval(s)
# c = b[0]
# print c[10002]

def getStrNumber(totaldam):
    total = str(totaldam)
    if totaldam >= 100000000:
        result = total[:-8] + u'亿' + total[-8:-4] + u'万'
    elif 10000 <= totaldam < 100000000:
        result = total[:-4] + u'万'
    else:
        result = total
    return result


print getStrNumber(110011110)
