#!/usr/bin/python
# coding: UTF-8

from pyexcel_xls import get_data

def read_xls_file():
    xls_data = get_data(r"E:\\dd.xlsx")
    print "Get data type:", type(xls_data)
    for sheet_n in xls_data.keys():
        print sheet_n, ":", xls_data[sheet_n]


if __name__ == '__main__':
    read_xls_file()
