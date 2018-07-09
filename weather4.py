#coding:utf-8 
import urllib2 
import json 
import time
def weather():

    url = 'http://www.weather.com.cn/adat/sk/101280601.html' # 101280601 深圳编码号 
      
    re = urllib2.urlopen(url).read() 
    re = re.decode('UTF-8') 
    we = json.loads(re)['weatherinfo']       
    print u'城市:' + we['city'] 
    print u'发布时间:' + we['time'] 
    print u'天气温度:' + we['temp'] +u'摄氏度'
    print u'风向:' + we['WD'] 
    print u'风力:' + we['WS'] 
    print u'相对湿度:' + we['SD'] 
    print u'播报时间:' + time.ctime()


weather()
