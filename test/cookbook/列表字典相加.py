#!/usr/bin/python
# coding: UTF-8
rt1 = ['a', 'b']
rt2 = [{'a': 1, 'b': 2, 'c': 3, 'd': 4}, {'d': 3, 'a': 3, 'b': 3, 'c': 4}, {'d': 1, 'b': 1, 'c': 3, 'a': 2},
       {'a': 5, 'c': 6, 'd': 3, 'b': 0}]
result = [dict([(k, item[k]) for k in rt1]) for item in rt2]
print result
result = [(k, [x[k] for x in rt2]) for k in rt1]
print result
result = [(k, sum([x[k] for x in rt2])) for k in rt1]
print result

a = ['templateId', 'amount']
b = [{"amount": 1, "templateId": 20100}, {"amount": 1, "templateId": 20100}, {"amount": 1, "templateId": 10003},
     {"amount": 1, "templateId": 10003}, {"amount": 1, "templateId": 10003}]
# 默认字典
d = {}
f = []

for _id, amount in d.items():
    f.append({"templateId": _id, "amount": amount})
print f

result = [{"templateId": _id, "amount": amount} for _id, amount in d.items()]
print result