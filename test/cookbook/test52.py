# coding:utf-8
# !/user/bin/python


def calc(n):
    total = n / 2  # 可以买到的瓶数
    ping = total
    gai = total
    if total == 0:
        return 0
    else:
        while ping / 2 > 0 or gai / 4 > 0:
            if ping / 2 > 0:
                tmp = ping / 2
                total = total + tmp
                gai = gai + tmp
                ping = ping % 2
                ping += tmp
            elif gai / 4 > 0:
                tmp = gai / 4
                total = total + tmp
                ping = ping + tmp
                gai = gai % 4
                gai += tmp
    return total, ping, gai

print calc(10)
