#!/usr/bin/python
# coding: UTF-8
import re

text = 'yeah, but no, but yeah, but no, but yeah'
text = 'yeah, but no, but yeah, but no, but yeah'
# Exact match
# print text == 'yeah'
# # Match at start or end
# print text.startswith('yeah')
# print text.endswith('no')
# # Search for the location of the first occurrence
# print text.find('no')

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
# Simple matching: \d+ means match one or more digits
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')
if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')

# 编辑成模型对象直接匹配
datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')

if datepat.match(text2):
    print('yes')
else:
    print('no')
