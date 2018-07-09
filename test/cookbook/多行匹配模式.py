#!/usr/bin/python
# coding: UTF-8
import re

comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a
multiline comment */
'''
print comment.findall(text1)
print comment.findall(text2)
# 为了修正这个问题，你可以修改模式字符串，增加对换行的支持。比如：
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print comment.findall(text2)
# re.compile() 函数接受一个标志参数叫 re.DOTALL ，在这里非常有用。 它可以让正则表
# 达式中的点(.)匹配包括换行符在内的任意字符。比如：
comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print comment.findall(text2)
