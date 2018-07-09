#!user/bin/python
# encoding:utf-8
import time

rewardResult = ({'rankReward': u'31041;300|73000;10|11002;300000', 'rank': u'1|1', 'limit': 3000L, 'activity': 40001L,
                 'tips': u'H\\u1ea1ng 1', 'id': 40001001L},
                {'rankReward': u'31041;200|73000;5|11002;200000', 'rank': u'2|3', 'limit': 2000L, 'activity': 40001L,
                 'tips': u'H\\u1ea1ng 2~3', 'id': 40001002L},
                {'rankReward': u'31041;100|73000;3|11002;100000', 'rank': u'4|6', 'limit': 1200L, 'activity': 40001L,
                 'tips': u'H\\u1ea1ng 4~6', 'id': 40001003L},
                {'rankReward': u'31041;60|73000;2|11002;50000', 'rank': u'7|10', 'limit': 800L, 'activity': 40001L,
                 'tips': u'H\\u1ea1ng 7~10', 'id': 40001004L},
                {'rankReward': u'31041;30|73000;1|11002;30000', 'rank': u'11|20', 'limit': 400L, 'activity': 40001L,
                 'tips': u'H\\u1ea1ng 11~20', 'id': 40001005L})


def a():
    b = int(rewardResult[::-1][0].get('rank').split('|')[1]) if rewardResult[::-1][0].get('rank') else 30
    return b


print a()
