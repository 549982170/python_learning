#!user/bin/python
#encoding:utf-8
import urllib2
import re

f = open("c:\Users\mx-yzw\Desktop\out.csv",'w')
for line in open("c:\Users\mx-yzw\Desktop\word.txt"):
    word,address = line.split()
    print "\n--------" + word,address,
    url = "http://www.haosou.com/s?ie=utf-8&shb=1&src=360sou_newhome&q=" + word
    response = urllib2.urlopen(url)
    html = response.read()
    if address in html:        
        text = address+'.*?res([0-9]*)'
        m = re.search(text, html, re.IGNORECASE)
        result = m.group(1)
        print "-----------ok",
    else:
        result = "Not found!"
        print "-----------!!!!!!!!----- fail",
    f.write(word+","+address+","+result+"\n")
f.close()