#!user/bin/python
#encoding:utf-8
a={1:1,2:2,3:3}
#print ','.join(a.keys())
b=list(a.keys())

for i in range(len(b)):
	b[i]=str(b[i])

print ','.join(b) #Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串
