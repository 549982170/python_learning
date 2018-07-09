# coding:utf-8
# !/user/bin/python
import os


def changedoc2docxbywin32(fpath, tpath):
    """把doc文件转换为docx因为用到win32com,所以仅支持windows系统
    @param fpath: 文件绝对路径,不能包含中文
    @param tpath: 文件绝对保存路径,不能包含中文"""
    try:
        from win32com import client
        import pythoncom
        pythoncom.CoInitialize()
        word = client.DispatchEx('Word.Application')  # 独立进程
        word.Visible = 0  # 不显示
        word.DisplayAlerts = 0  # 不警告
        doc = word.Documents.Open(fpath)
        doc.SaveAs(tpath, 12)  # 参数16是保存为doc,转化成docx是12
        doc.Close()
        word.Quit()
        return True
    except:
        if doc:
            doc.Close()
        word.Quit()
        return False

