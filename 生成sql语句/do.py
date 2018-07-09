#!/usr/bin/env python
# coding:utf8

try:
    with open("1.txt") as f:
        result = list()
        result2 = list()
        for line in f.readlines():  # 依次读取每行
            line = line.strip()  # 去掉每行头尾空白
            if not len(line) or line.startswith('#'):  # 判断是否是空行或注释行
                continue  # 是的话，跳过不处理
            result.append("`"+line+"`")  # 保存
            result2.append("ca['"+line+"']")  # 保存
        d = ','.join(result)
        s = ','.join(['"%s"'] * len(result))
        t = ','.join(result2)
        print "sql =" + "\'insert into " + "test" + "(" + d + ")" + " values(" + s + ")\'" + "%(" + t + ")"
except:
    pass
