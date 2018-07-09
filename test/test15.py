#!user/bin/python
# encoding:utf-8
import hashlib
def md5(ss):
    m = hashlib.md5()
    m.update(ss)
    return m.hexdigest()
# a='10001'+'1'+'1468998187'
# print md5(a)

a=[(50003L, {'info': u'288|688|1488|3288|7888|15888|30888|50888', 'openTime': u'10005',
            'show': u'188|388|888|2088|5088|10888|20888|35888', 'goldReward': u'0|0|0|0|5|7|9|10',
            'roleTime':  None, 'overTime': u'1', 'vip': u'20160719 5:00', 'cost': u'20160726 5:00',
            'tips': u'226,254|474,505|1048, 1119|2464,2610|5648,6004|11868,12652|22768,24022|39657,41092',
            'id': 50003L})]

for aic , d in a:
    print aic , 'ss',d