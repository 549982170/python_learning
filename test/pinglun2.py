url = 'http://www.yl1001.com/ajax.htm?doaction=xinzhi_ajax&detail=reply&position=php'
query_args = {
      "bcontents" : "原来如此",
      "code" : "wlgs",
      "article_id" : "1261413975938720",
      "content" : "原来如此",
      "group_id" : "0",
      "article_source" : "userzone",
      "cks" : "34783dc58bebdce786f68a116cd0ac1e",
      "ajaxformflag" : "1"
}
r = s.post(url, data=query_args)
print r.content


print time.ctime()
print "The message is OK" 