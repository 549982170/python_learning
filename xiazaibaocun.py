import urllib
def cbk(a, b, c): 
    '''�ص�����
    @a: �Ѿ����ص����ݿ�
    @b: ���ݿ�Ĵ�С
    @c: Զ���ļ��Ĵ�С    ''' 
    per = 100.0 * a * b / c 
    if per > 100: 
        per = 100 
    print '%.2f%%' % per
url = 'http://www.baidu.com'
local = 'f://123'
urllib.urlretrieve(url, local, cbk)
