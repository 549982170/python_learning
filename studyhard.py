#coding=utf-8
import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" alt'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist

html = getHtml("http://www.moxian.com")

print getImg(html)