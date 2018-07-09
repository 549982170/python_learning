#!/usr/bin/python
# coding: UTF-8
text = 'Hello World'
print text.ljust(20)
print text.rjust(20)
print text.center(20)
# 接受可填充的值
print text.rjust(20, '=')
print text.center(20, '*')
# 另外的对齐形式
print format(text, '>20')
print format(text, '<20')
print format(text, '^20')
# 指定非空填充字符
print format(text, '=>20s')
print format(text, 's<20s')
print format(text, '*^20s')
# 当格式化多个值的时候，这些格式代码也可以被用在 format() 方法中
print '{:>10s} {:>10s}'.format('Hello', 'World')
# 格式化数字
x = 1.2345
print format(x, '>10')
print format(x, '^10.2f')
