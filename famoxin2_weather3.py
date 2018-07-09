#!user/bin/python
#encoding:utf-8

import time
import requests
import json
import urllib2
import gzip
import StringIO
def run():
   # for i in range(2):
        agent="Mozilla/5.0 (X11; U; Linux i686 (x86_64); zh-CN; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2"
        s = requests.Session()
        s.headers.update({'User-Agent': agent})
        
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
        fl = data_dict.get('data').get('yesterday').get('fl')+'\n'
        yesterday = u'昨天天天气情况：\n日期：'+data+u'天气情况：'+type+u'最高温度：'+high+u'最低温度：'+low+u'风向：'+fx+u'风力：'+fl
        #print yesterday       
        
        city = data_dict.get('data').get('city')+'\n'       #当天天气
        wendu = data_dict.get('data').get('wendu')+u'℃\n'
        aqi = data_dict.get('data').get('aqi')+u'%'+'\n'
        ganmao = data_dict.get('data').get('ganmao')+'\n'
        todayweather = u'今天天气情况：\n城市：'+city+u'温度：'+wendu+u'相对湿度：'+aqi+u'温馨提示：'+ganmao
        #print todayweather
                
        forecast_five_day = u'未来五天天气情况：\n'            #未来五日天气
        for i in data_dict.get('data').get('forecast'): 
                date = u'日期：'+i.get('date')+u'；'
                type = u'天气情况：'+i.get('type')+u'；'
                high = u'最高温度：'+i.get('high')+u'；'
                low = u'最低温度：'+i.get('low')+u'；'    
                fengxiang = u'风向：'+i.get('fengxiang')+u'；'
                fengli = u'风力：'+i.get('fengli')+u'。'
                forecast_day = date+type+high+low+fengxiang+fengli 
                forecast_five_day+=forecast_day 
        #print forecast_five_day
        weather = yesterday+todayweather+forecast_five_day+u'\n发布时间：'+time.ctime()     #全部天气情况
      
        print time.ctime()
        url = 'http://moxian.com/user/ajax/firstlogin'
        query_args = {
             'login_type': '1',
             'user_name': '18998405382',
             'user_pwd': '8f38563d476fdbce3142554d0ca75482',
             'keeplogin': 'off',
             "country_num": "86"
        }
        
        r = s.post(url, data=query_args)
        print r.json()
        code = r.json()['data']
        
        url = 'http://moxian.com/user/ajax/secondlogin'
        query_args = {
             'login_type': '1',
             'user_name': '18998405382',
             'keeplogin': 'off',
             'verify_code': code,
             'redirect_url': 'true',
             "country_num": "86"
        }
        r = s.post(url, data=query_args)
        #print r.json()
        #print r.cookies
        
        url = 'http://moxian.com/main/gateway.php'
        query_args = {
              "type": "add_info",
              "pics[]":"http://rs.moxian.com/upload/2015/20150320/460242/201503201155146063.jpg",
              "desc[]": weather,
              "type_id": "0",
              "tags[]": "la_2688",
              "info_local": ""
        }
        r = s.post(url, data=query_args)
        print r.content
        
        print time.ctime()
        print "The message is OK" 

if __name__ == '__main__':
        run()
