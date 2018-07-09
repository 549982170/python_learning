#coding:utf-8 
import urllib2 
import json 

def weather():

    url = 'http://www.weather.com.cn/adat/cityinfo/101280601.html' # 101280601 深圳编码号 
      
    re = urllib2.urlopen(url).read() 
    re = re.decode('UTF-8') 
    we = json.loads(re)['weatherinfo']       
    print u'城市:' + we['city'] 
    print u'发布时间:' + we['ptime'] 
    print u'天气情况:' + we['weather'] 
    print u'天气温度:' + we['temp2'] + '-' + we['temp1']


weather()
