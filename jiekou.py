import urllib    
import urllib2    
  
url = 'http://www.someserver.com/register.cgi'    
    
values = {'name' : 'WHY',    
          'location' : 'SDU',    
          'language' : 'Python' }    
  
data = urllib.urlencode(values) # ���빤��  
req = urllib2.Request(url, data)  # ��������ͬʱ��data��  
response = urllib2.urlopen(req)  #���ܷ�������Ϣ  
the_page = response.read()  #��ȡ����������  
print the_page