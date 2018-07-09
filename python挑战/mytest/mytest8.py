# encoding:utf-8
# usr/bin/python

def fun_1(data):
    def fun_2(data_2):
        return data, data_2

    return fun_2


b = fun_1(123)
print b(123)
