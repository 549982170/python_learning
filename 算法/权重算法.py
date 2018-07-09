#!user/bin/python
# encoding:utf-8
import random


def randomItem(itemWgt):
    '''随机一个物品，返回物品ID, 数量
    @param itemWgt: 道具1ID,数量|道具2ID,数量，例：30001,1|30002,2
    '''
    itemList = itemWgt.split('|')
    tmpArr = itemList[random.randint(0, len(itemList) - 1)].split(',')
    return int(tmpArr[0]), int(tmpArr[1])  # 道具ID，数量


def randomRate(itemWgt, ignoreList=[]):
    '''随机一个物品，返回物品ID
    @param itemWgt: 道具1ID,概率|道具2ID,概率，例：30001,30|30002,70
    @param ignoreList: 需要排除的道具ID列表，itemWgt不能出现相同道具ID
    '''
    totalWeight = 0
    itemList = itemWgt.split('|')
    if len(itemList) == 0: return -1
    for item in itemList:
        tmplist = item.split(',')
        itemId = int(tmplist[0])
        weight = int(tmplist[1])
        if itemId in ignoreList:
            continue
        totalWeight += weight

    step = 1
    randval = random.randint(1, totalWeight)
    for item in itemList:
        tmplist = item.split(',')
        itemId = int(tmplist[0])
        weight = int(tmplist[1])
        if step <= randval and randval < step + weight:
            if itemId in ignoreList:
                continue
            return itemId
        else:
            step += weight
    return -1


def randomItemRate(itemWgt):
    '''随机一个物品，返回物品ID
    @param itemWgt: 道具1ID,数量,概率|道具2ID,数量,概率，例：30001,1,30|30002,1,70
    '''
    totalWeight = 0
    itemList = itemWgt.split('|')
    if len(itemList) == 0: return -1, 0
    for item in itemList:
        tmplist = item.split(',')
        itemId = int(tmplist[0])
        weight = int(tmplist[2])
        totalWeight += weight
    step = 1
    randval = random.randint(1, totalWeight)
    for item in itemList:
        tmplist = item.split(',')
        itemId = int(tmplist[0])
        amount = int(tmplist[1])
        weight = int(tmplist[2])
        if step <= randval and randval < step + weight:
            return itemId, amount
        else:
            step += weight
    return -1, 0


def randomItemSub(itemWgt, ignoreList=[]):
    '''随机一个物品，返回物品ID和物品的下标
    @param itemWgt: 道具1ID,数量,概率|道具2ID,数量,概率，例：30001,1,30|30002,1,70
    '''
    totalWeight = 0
    itemList = itemWgt.split('|')
    if len(itemList) == 0: return -1, 0, 0
    for sub, item in enumerate(itemList):
        tmplist = item.split(',')
        itemId = int(tmplist[0])
        weight = int(tmplist[2])
        if sub in ignoreList:
            continue
        totalWeight += weight

    step = 1
    randval = random.randint(1, totalWeight)
    for sub, item in enumerate(itemList):
        tmplist = item.split(',')
        itemId = int(tmplist[0])
        amount = int(tmplist[1])
        weight = int(tmplist[2])
        if step <= randval and randval < step + weight:
            if sub in ignoreList:
                continue
            return sub, itemId, amount
        else:
            step += weight
    return -1, 0, 0
