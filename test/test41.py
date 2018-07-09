#!/usr/bin/env python
# encoding:utf8
def checkpermission(checknum, permission):
    """
    @param checknum: 检测的十进制权限值
    @param permission: 拥有的权值值"""
    checknum2 = bin(checknum).replace("0b", "")
    permission2 = bin(permission).replace("0b", "")
    print checknum2, permission2
    print checknum & permission

    print checknum | permission

checkpermission(1, 14)



