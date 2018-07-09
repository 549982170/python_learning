#!/usr/bin/python
# coding: UTF-8

# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

html = '''<dict>
        <key>LogType</key>
        <string>Default</string>
        <key>Message</key>
        <string>测试场景:订餐提交页面</string>
        <string>Loop in : 2 durTime:0.266s</string>
        <key>Timestamp</key>
        <date>2014-06-06T12:16:24Z</date>
        <key>Type</key>
        <integer>1</integer>
</dict>'''

soup = BeautifulSoup(html)
trs = soup.findAll("string")
length = len(trs)
arr = []
for i in range(length):
    print trs[i].contents