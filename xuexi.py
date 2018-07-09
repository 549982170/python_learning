#coding=utf-8
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    #reg = r'src="(.+\.jpg)"pic

html = getHtml("http://www.baidu.com")

print html