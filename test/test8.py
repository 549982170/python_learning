#!/usr/bin/python
# coding: utf-8
a = "[]"
b = "[{10002: [1001, 1002]}, {10001: [2001, 2002]}, {10003: [2003, 3001]}]"


def BPBossReward(rewardList, rewardedList):
    rewardList = eval(str(rewardList))
    rewardedList = eval(str(rewardedList))
    reward = {}
    rewarded = {}
    if rewardList:
        reward = rewardList[0]
        key = reward.keys()[0]
        rewarded[key] = []
        for i in rewardedList:
            if i.keys()[0] == key:
                rewarded = i
                break
    else:
        if rewardedList:
            for i in rewardedList[-1:]:
                rewarded = i
                reward[i.keys()[0]] = []
                break
    return reward, rewarded


c, d = BPBossReward(a, b)
print c
# print "\n"
print d
