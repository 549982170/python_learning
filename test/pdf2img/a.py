#!/usr/bin/python
import imgkit

config = imgkit.config(wkhtmltoimage='D:\\wkhtmltopdf\\bin\\wkhtmltoimage.exe')
body = """
<html>
  <head>
    <meta name="imgkit-format" content="png"/>
    <meta name="imgkit-orientation" content="Landscape"/>
  </head>
  Hello World!
  </html>
"""
options = {
    'page-size': 'Letter',
    # 'margin-top': '0.75in',
    # 'margin-right': '0.75in',
    # 'margin-bottom': '0.75in',
    # 'margin-left': '0.75in',
    'encoding': "UTF-8",
    'no-outline': None,
    'quiet': ''
}

imgkit.from_string(body, 'out.png', options=options, config=config)
