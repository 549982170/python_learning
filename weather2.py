#! /usr/bin/python  
# -*- coding: cp936 -*-  
# coding = utf-8  
  
# ToDo: get weather info from weather.com.cn  
# Author: Steven  
# Date: 2013/05/13  
  
import urllib2  
import json  
  
# get weather html and parse to json  
weatherHtml = urllib2.urlopen('http://m.weather.com.cn/data/101200101.html').read()  
weatherJSON = json.JSONDecoder().decode(weatherHtml)  
weatherInfo = weatherJSON['weatherinfo']  
  
# print weather info  
print '���У�\t', weatherInfo['city']  
print 'ʱ�䣺\t', weatherInfo['date_y']  
print '24Сʱ������'  
print '�¶ȣ�\t', weatherInfo['temp1']  
print '������\t', weatherInfo['weather1']  
print '���٣�\t', weatherInfo['wind1']  
print '�����ߣ�\t', weatherInfo['index_uv']  
print '����ָ����\t', weatherInfo['index_d']  
print '48Сʱ������'  
print '�¶ȣ�\t', weatherInfo['temp2']  
print '������\t', weatherInfo['weather2']  
print '���٣�\t', weatherInfo['wind2']  
print '�����ߣ�\t', weatherInfo['index48_uv']  
print '����ָ����\t', weatherInfo['index48_d']  
print '72Сʱ������'  
print '�¶ȣ�\t', weatherInfo['temp3']  
print '������\t', weatherInfo['weather3']  
print '���٣�\t', weatherInfo['wind3']  