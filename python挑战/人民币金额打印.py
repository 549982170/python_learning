# coding:utf-8
# !/user/bin/python
""""
银行在打印票据的时候，常常需要将阿拉伯数字表示的人民币金额转换为大写表示，现在请你来完成这样一个程序。

在中文大写方式中，0到10以及100、1000、10000被依次表示为：    零 壹 贰 叁 肆 伍 陆 柒 捌 玖 拾 佰 仟 万

以下的例子示范了阿拉伯数字到人民币大写的转换规则：

1	壹圆

11	壹拾壹圆

111	壹佰壹拾壹圆

101	壹佰零壹圆

-1000	负壹仟圆

1234567	壹佰贰拾叁万肆仟伍佰陆拾柒圆

现在给你一个整数a(|a|<100000000), 请你打印出人民币大写表示.

例如：a=1

则输出：壹圆
"""
a = 100000

N = {0: '零', 1: '壹', 2: '贰', 3: '叁', 4: '肆', 5: '伍', 6: '陆', 7: '柒', 8: '捌', 9: '玖'}
M = ['亿', '仟', '佰', '拾', '萬', '仟', '佰', '拾', '圆']


def fun(a):
    if len(str(a)) > 9:
        print 'the number is to long'
    b = abs(a)
    new = []
    for st in str(b):
        if int(st) in N.keys():
            new.append(N[int(st)])
    l = M[-len(new):]
    s = ''
    for x, y in zip(new, l):
        s += x + y
    if a < 0:
        return u'负' + s.decode('utf8')
    else:
        return s.decode('utf8')


print fun(a)

chn = ["零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖", "", "拾", "佰", "仟", "万"]


def f(n):
    t = []
    str = ""
    flag = 0  # 是否有连续0的标记
    while n:
        t.append(n % 10)
        n /= 10
    i = len(t) - 1
    for tmpi in range(i, -1, -1):
        if t[tmpi] != 0:
            if flag == 1:
                str += chn[0]
                flag = 0
            str += chn[t[tmpi]] + chn[tmpi + 10]
        elif flag == 0:
            flag = 1
    return str


def money(a):
    mstr = ''
    if a < 0:
        mstr += "负"
        a = -a
    elif a == 0:
        mstr = "零"  # .decode("utf8")
    else:
        nh = a / 10000
        nl = a % 10000
        if nh != 0:
            mstr = mstr + f(nh) + "万"
            if (nh % 10 == 0 or nl / 1000 == 0) and nl != 0:
                mstr += "零"
        if nl != 0:
            mstr += f(nl)
    mstr += "圆"
    return mstr


print money(a).decode("utf8")


