#!/usr/bin/python
# -*- coding: utf-8 -*-
#CreateDate: 2015-03-12


import requests
import BeautifulSoup as bs


key_word = '.gov.cn'
words = []
with open('C:\Users\mx-yzw\Desktop\word2.txt') as file: # file must utf-8 format
    word = file.readlines()
    words.extend(word)
    
    agent="Mozilla/5.0 (X11; U; Linux i686 (x86_64); zh-CN; rv:1.9.1.2)Gecko/20090729 Firefox/3.5.2"
    s = requests.Session()
    s.headers.update({'User-Agent': agent}) 
    
    
    result=[]
for word in words:
    payload = {'q':word.strip()} 
    url = 'http://www.haosou.com/s?ie=utf-8&shb=1&src=360sou_newhome'
    r = s.get(url, params=payload)
    cont = r.text
    soup = bs.BeautifulSoup(cont)
    top_div = soup.findAll('li',{"class":"res-list"})

for x in top_div:
    a = x.a
    url = a.get("href")

    if key_word in url:
        result.append(word)
        break 
    
    for x in result:
        print x