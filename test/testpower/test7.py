#!/usr/bin/python
# coding: UTF-8
def is_chinese(contents):
    """判断是否仅为中文"""
    try:
        for ca in contents:
            if ca <= u"\u4e00" or ca >= u"\u9fa6":
                return False
        return True
    except:
        return False


ss = "中文测试测试请说ha".decode("utf-8")

# for row in ss:
#     print row, is_chinese(row)

print is_chinese(ss)
