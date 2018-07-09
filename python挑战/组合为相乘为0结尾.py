# coding:utf-8
# !/user/bin/python
""""给你一个正整数列表 L, 输出L内所有数字的乘积末尾0的个数。(提示:不要直接相乘,数字很多,相乘得到的结果可能会很大)。

例如:L=[2,8,3,50],

则输出:2"""
countof2 = 0

countof5 = 0
L = [2, 8, 3, 50]
for i in L:
    while (i % 2 == 0):
        i = i / 2
        countof2 += 1
    while (i % 5 == 0):
        i = i / 5
        countof5 += 1
print min(countof2, countof5)
