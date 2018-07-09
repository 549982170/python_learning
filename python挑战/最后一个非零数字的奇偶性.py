# coding:utf-8
# !/user/bin/python
""""给你一个正整数列表 L, 判断列表内所有数字乘积的最后一个非零数字的奇偶性。如果为奇数输出1,偶数则输出0.。

例如：L=[2,8,3,50]

则输出:0"""

L = [2, 8, 3, 50]


def splitList(L):
    count_2 = 0
    count_5 = 0
    for item in L:
        while (item % 2 == 0):
            count_2 += 1;
            item = item / 2;
        while (item % 5 == 0):
            count_5 += 1;
            item = item / 5;

    return count_2, count_5


# 其实最后发现返回最终到列表没什么用;

count2, count5 = splitList(L)
# 下面判断最后一个非零数字的奇偶性,如果质因数中5的个数比2多，说明2已经用完了，最终得到到就是奇数，否则是偶数;
if count2 > count5:
    print 0
else:
    print 1
