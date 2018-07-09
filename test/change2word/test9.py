#!/usr/bin/python
# coding: UTF-8

def changInt2bit(num_2, digit=0):
    """十进制转2进制"""
    try:
        return int("0b" + str(num_2), 2)  # 转为10进制
    except:
        return 0


def changInt2Bit(num, tip=16):
    """十进制转二进制,八进制,16进制"""
    try:
        num = int(num)
        if tip == 2:
            return bin(num)  # 十进制转二进制
        if tip == 8:
            return oct(num)  # 十进制转八进制
        if tip == 16:
            return hex(num)  # 十进制转十六进制
        else:
            return int(num)  # 十进制转十进制
    except:
        return 0


print changInt2Bit('10', 2)
