#!/usr/bin/env python
# encoding:utf8
from docx import Document

fname = "D:\\workerspace\\Soovii.ProductionPlanning\\src\\app\\media\\upload\\docx\\20170221\\5f6cd700-f81c-11e6-a69e-28565a809039.docx"

f = open(fname, 'rb+')
print f
paras = Document(fname)
docText = '\n'.join([paragraph.text.encode('utf-8') for paragraph in paras.paragraphs])
print docText
