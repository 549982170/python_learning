#!/usr/bin/env python
#-*- encoding: utf-8 -*-
import urllib2
import gzip
import StringIO
import json
import time
url = r'http://wthrcdn.etouch.cn/weather_mini?citykey=101280601'# 101280601 深圳编码号
response = urllib2.urlopen(url)
stream = StringIO.StringIO(response.read())
with gzip.GzipFile(fileobj=stream) as f:            #gzip解压
    data = f.read()


data_dict = json.loads(data)#把返回的json当字典处理

data = data_dict.get('data').get('yesterday').get('date')+'\n'      #昨天天气 
type = data_dict.get('data').get('yesterday').get('type')+'\n'
high = data_dict.get('data').get('yesterday').get('high')+'\n'
low = data_dict.get('data').get('yesterday').get('low')+'\n'
fx = data_dict.get('data').get('yesterday').get('fx')+'\n'
fl = data_dict.get('data').get('yesterday').get('fl')+'\n\n'
yesterday = u'昨天天天气情况：\n日期：'+data+u'天气情况：'+type+u'最高温度：'+high+u'最低温度：'+low+u'风向：'+fx+u'风力：'+fl
#print yesterday


city = data_dict.get('data').get('city')+'\n'       #当天天气
wendu = data_dict.get('data').get('wendu')+'\n'
aqi = data_dict.get('data').get('aqi')+'\n'
ganmao = data_dict.get('data').get('ganmao')+'\n\n'
todayweather = u'今天天气情况：\n城市：'+city+u'温度：'+wendu+u'相对湿度：%'+aqi+u'温馨提示：'+ganmao
#print todayweather
 


forecast_five_day = u'未来五天天气情况：\n'            #未来五日天气
for i in data_dict.get('data').get('forecast'): 
    date = u'日期：'+i.get('date')+'\n'
    type = u'天气情况：'+i.get('type')+'\n'
    high = u'最高温度：'+i.get('high')+'\n'
    low = u'最低温度：'+i.get('low')+'\n'    
    fengxiang = u'风向：'+i.get('fengxiang')+'\n'
    fengli = u'风力：'+i.get('fengli')+'\n'
    forecast_day = date+type+high+low+fengxiang+fengli+'\n'   
    forecast_five_day+=forecast_day 
#print forecast_five_day

weather = yesterday+todayweather+u'\n发布时间：'+forecast_five_day+u'\n发布时间：'+time.ctime()     #全部天气情况

print weather
