import urllib    
import urllib2    
  
url = 'http://www.someserver.com/register.cgi'    
    
values = {'name' : 'WHY',    
          'location' : 'SDU',    
          'language' : 'Python' }    
  
data = urllib.urlencode(values) # 编码工作  
req = urllib2.Request(url, data)  # 发送请求同时传data表单  
response = urllib2.urlopen(req)  #接受反馈的信息  
the_page = response.read()  #读取反馈的内容  
print the_page