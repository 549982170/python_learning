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

        '''
        time_stamp = int (round(time.time(),0))  #直接转换为整形
        
        time_stamp = str(time_stamp)
        print time_stamp
        '''
        url = 'http://japi.juhe.cn/joke/content/text.from?key=e2b1d4fbaf2f02a49d331355c6792f42&page=1&pagesize=20'
        result = urllib2.urlopen(url).read()
        
       # print result
        result = json.loads(result,'utf-8')  #把返回的json当字典处理
        message = u'每日20个笑话：\n'
        x = 1
        for i in result.get('result').get('data'):        
                Number = str(u'NO:%d'% (x))
                content = Number+i.get('content')+u'\n'
                x+=1
            #    print content
                message += content
        
       
        #print message
        
        

        
                
      
                



     

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
              "desc[]": message,
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
