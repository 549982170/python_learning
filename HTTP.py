# -*- coding:gb2312 -*-
import urllib2,urllib,xlrd
def GetUserInfo(uname,method):
    if method == 'GET':
        url = 'http://ip:port/interface/GetUserInfo.php?uname='+urlcode(uname)
        result = urllib2.urlopen(url).read()
        return result
   
    if method == 'POST':
        url = 'http://ip:port/interface/GetUserInfo.php'
        values = {'uname' : uname}
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        result = response.read()
        return result
def GetUser():
    bk = xlrd.open_workbook(excel文件名称) # 打开excel文件
    sh = bk.sheet_by_name(excel表名)# 打开excel表
    nrows = sh.nrows # 获取总行数
    for i in range(1,nrows):  
        TestCase = sh.cell_value(i,0)
        uname = sh.cell_value(i,1)
        method = sh.cell_value(i,2)
        EX_Result=sh.cell_value(i,3)
        WriterLog('Testcase Name:'+TestCase+'TestData: uname = '+uname+' ,method = '+method+' ,EX_Result = ' + ,EX_Result) # 写测试日志
        AC_result = GetUserInfo(uname,method) # 调用API接口
        WriterLog('AC_result = ' + AC_result) # 写测试日志
        if EX_Result == AC_result: #实际结果与预期结果对比
            WriterLog(...) #写测试日志
            WriterReport(...)#写测试报告
        else
            WriterLog(...)#写测试日志
            WriterReport(...)#写测试报告