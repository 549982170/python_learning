# encoding:utf-8
s = "[]"
b = "[{10002:[11,22]},{10001:[11,22]},{10003:[11,22]}]"

def BPBossReward(rewardList, rewardedList):
    rewardList = eval(rewardList)
    rewardedList = eval(rewardedList)
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
            for i in rewardedList:
                rewarded = i
                reward[i.keys()[0]] = []
                break
    return reward, rewarded


print BPBossReward(s, b)

# a = c = b
# print a, c
