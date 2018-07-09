#!user/bin/python
# encoding:utf-8
import imgkit

imgkit.from_url('https://www.baidu.com/', 'D:\\python_learning\\test\\pdf2img\\out.jpg')
# imgkit.from_file('test.html','D:\\python_learning\\test\\pdf2img\\out2.jpg')
imgkit.from_string('Hello!', 'D:\\python_learning\\test\\pdf2img\\out3.jpg')