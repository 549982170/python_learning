# coding:utf-8
# !/user/bin/python
import pdfkit
path_wkthmltopdf = 'D:\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
pdfkit.from_url('http://www.baidu.com', 'out.pdf',configuration=config)

