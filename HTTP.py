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
    bk = xlrd.open_workbook(excel�ļ�����) # ��excel�ļ�
    sh = bk.sheet_by_name(excel����)# ��excel��
    nrows = sh.nrows # ��ȡ������
    for i in range(1,nrows):  
        TestCase = sh.cell_value(i,0)
        uname = sh.cell_value(i,1)
        method = sh.cell_value(i,2)
        EX_Result=sh.cell_value(i,3)
        WriterLog('Testcase Name:'+TestCase+'TestData: uname = '+uname+' ,method = '+method+' ,EX_Result = ' + ,EX_Result) # д������־
        AC_result = GetUserInfo(uname,method) # ����API�ӿ�
        WriterLog('AC_result = ' + AC_result) # д������־
        if EX_Result == AC_result: #ʵ�ʽ����Ԥ�ڽ���Ա�
            WriterLog(...) #д������־
            WriterReport(...)#д���Ա���
        else
            WriterLog(...)#д������־
            WriterReport(...)#д���Ա���