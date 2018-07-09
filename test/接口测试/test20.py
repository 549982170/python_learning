#!/usr/bin/env python
# coding:utf8
import json

a = {'userId': 64169, 'nickName': r'rầĩÂTrầốiệpa', 'channelId': 1001, 'petId': 41099}
b = json.dumps(a)
c = json.loads(b)
print c
nickName = c.get('nickName')
d = nickName.replace("'", "")
print d.strip('\n').strip('\r').strip('\t').strip(' ').replace("'", "")
# nickName = a.strip('\n').strip('\r').strip('\t').strip(' ')
# print nickName
