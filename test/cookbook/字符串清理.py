#!/usr/bin/env python
# encoding:utf8
import unicodedata

s = u'pýtĥöñ\fis\tawesome\r\n'
b = unicodedata.normalize('NFD', s)
c = b.encode('ascii', 'ignore').decode('ascii')
print c