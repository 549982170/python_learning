#!/usr/bin/python
# coding: UTF-8
import unicodedata
import sys
# Whitespace stripping
s = ' hello world \n'
print s.strip()
print s.lstrip()
print s.rstrip()
# Character stripping
t = '-----hello====='
print t.lstrip('-')
print t.strip('-=')

s = 'pýtĥöñ\fis\tawesome\r\n'
print s
remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None  # Deleted.
}
a = s.translate(remap)
print a
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD', a)
print b