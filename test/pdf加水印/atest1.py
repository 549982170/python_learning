#!/usr/bin/env python

import pdfkit
from pyPdf import PdfFileWriter, PdfFileReader

dir = '/home/guangning/Documents/python_pdf'
infile1  = dir + '/test.html'
infile2  = dir + '/watermark.html'
outfile1 = dir + '/test.pdf'
outfile2 = dir + '/watermark.pdf'

# generate PDFs
options = {
    'page-size': 'A4',
    'orientation': 'Landscape',
    'encoding': 'utf-8',
}
pdfkit.from_file(infile1, outfile1, options=options)
pdfkit.from_file(infile2, outfile2, options=options)

# add watermark
input1 = PdfFileReader(file(outfile1, "rb"))
input2 = PdfFileReader(file(outfile2, "rb"))
output = PdfFileWriter()
watermark_page = input2.getPage(0)
for i in range(input1.getNumPages()):
    page = input1.getPage(i)
    page.mergePage(watermark_page)
    output.addPage(page)
outputStream = file(dir+'/output.pdf', "wb")
output.write(outputStream)
outputStream.close()