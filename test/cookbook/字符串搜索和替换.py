#!/usr/bin/python
# coding: UTF-8
import re
from calendar import month_abbr

text = 'yeah, but no, but yeah, but no, but yeah'
print text.replace('yeah', 'yep')

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)

# 如果你打算用相同的模式做多次替换，考虑先编译它来提升性能。比如：
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print datepat.sub(r'\3-\1-\2', text)


# 更复杂的
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))
print datepat.sub(change_date, text)

# 查看替换次数
newtext, n = datepat.subn(r'\3-\1-\2', text)
print newtext
print n