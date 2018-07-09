#!/usr/bin/env python
# encoding:utf8

def checkPermission(num, is2Str=False):
        """检测用户是否拥有权限
        @param num: (int)权限值,(十进制),当is2Str传入True时,传入为二进制数值01010100
        @param is2Str: (boolean),默认False,当传入True时,num必须传入二进制数值"""
        if is2Str is True:
            num = int(num, 2)  # 转为10进制
        else:
            num = int(num)
        RoleCode = 15  # 容错获取用户权限
        return num & RoleCode == num  # 拥有权限返回True,否则返回Flase


print checkPermission(4)