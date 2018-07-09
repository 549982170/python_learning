#!user/bin/python
#encoding:utf-8

import time
import requests
import json
import urllib,urllib2

def run():
   # for i in range(2):
        agent="Mozilla/5.0 (X11; U; Linux i686 (x86_64); zh-CN; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2"
        s = requests.Session()
        s.headers.update({'User-Agent': agent})
        

        url_1 = 'http://www.weather.com.cn/adat/sk/101280601.html' # 101280601 深圳编码号                  
        re = urllib2.urlopen(url_1).read() 
        re = re.decode('UTF-8') 
        we = json.loads(re)['weatherinfo']       
        #print u'城市:' + we['city'] 
        #print u'发布时间:' + we['ptime'] 
        #print u'天气情况:' + we['weather'] 
        #print u'天气温度:' + we['temp2']  + '-' + we['temp1'] 
        weather = u'城市:'+we['city']+'\n'+u'天气发布时间:'+we['time']+'\n'+u'天气温度:'+we['temp']+u'摄氏度'+'\n'+u'风向:'+we['WD']+'\n'+u'风力:'+we['WS']+'\n'+u'相对湿度:'+we['SD']+'\n'+u'播报时间：'+time.ctime()

        
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
        print r.json()
        print r.cookies
        
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
