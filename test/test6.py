#!/usr/bin/python
# coding: UTF-8
# a = [2001]
# b = [2001L, 2002L, 2003L]
# print a in b

a = "[{10002: [1001, 1002]}, {10001: [2001, 2002]}, {10003: [2003, 3001]}]"
sequence = eval(a)

sequence[0] = {10002: [1001]}

print sequence
# def checkrewardList(bossId, rewardId, rewardList):
#     for item in rewardList:
#         if item.has_key(bossId):
#             if rewardId in item[bossId]:
#                 return True
#     return False
#
#
# print checkrewardList("10002", "1001", sequence)

# for index, item in enumerate(sequence):
#     print index, item
# def getbossreward(self, rewardId):
#     '''领取BOSS奖励
#     -1 表示一键领取
#     '''
#     try:
#         canRewardList = []
#         sql = "select * from tb_boss_fight_record where characterId=%s and totalDam>0" % self.owner.characterId
#         queryResult = dbpool.querySql(sql, True)
#
#         if queryResult:
#             mytotalDam = queryResult[0]['totalDam']
#             rewardedList = eval(queryResult[0]['reward'])
#
#             canRewardList = []
#             for rid, rewardCfg in tb_boss_reward.items():
#                 if rewardCfg['type'] == 2 and rid not in rewardedList and mytotalDam >= rewardCfg['damage']:
#                     canRewardList.append(rid)
#
#             if rewardId > 0:
#                 if rewardId not in canRewardList:
#                     raise BusiException(0, u'数据校验失败')
#                 else:
#                     rewardCfg = tb_boss_reward.get(rewardId)
#                     for itemId, amount in rewardCfg['item'].items():
#                         self.owner.pack.addItem(itemId, amount)
#                     rewardedList.append(rewardId)
#             else:
#                 if len(canRewardList) == 0:
#                     raise BusiException(0, u'没有可领取的奖励')
#
#                 for rewardId in canRewardList:
#                     rewardCfg = tb_boss_reward.get(rewardId)
#                     for itemId, amount in rewardCfg['item'].items():
#                         self.owner.pack.addItem(itemId, amount)
#                 rewardedList = rewardedList + canRewardList
#         else:
#             raise BusiException(0, u'没有可领取的奖励')
#
#         self.rewardList = rewardedList
#         sql = "update tb_boss_fight_record set reward='%s' where characterId=%s" % (
#         str(rewardedList), self.owner.characterId)
#         dbpool.execSql(sql)
#
#         retdata = {}
#         retdata['reward'] = rewardedList
#         changeInfo = self.owner.pack.formatChangeInfo()
#         retdata['changeInfo'] = changeInfo
#         self.owner.updatePlayer()
#         return {'result': 1, 'msg': u'', 'data': retdata}
#     except BusiException, busiEx:
#         logger.error(traceback.format_exc())
#         return busiEx.getResponse()
#     except Exception as e:
#         logger.exception(e)
#         return {'result': 0, 'msg': u''}
