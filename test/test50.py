#!/usr/bin/env python
# encoding:utf8

class ApiException(Exception):
    def __init__(self, **kwargs):
        self.status = kwargs.get('status', 0)
        self.result = kwargs.get('result', 0)
        self.msg = kwargs.get('msg', u'未知错误')
        self.data = kwargs.get('data', {})
        self.kwargs = kwargs

    def __str__(self):
        ret = 'status: %s,result: %s, msg: %s, data: %s' % (self.status, self.result, self.msg, self.data)
        if isinstance(ret, unicode):
            ret = ret.encode('utf-8')
        return ret

    def toDict(self):
        return {'status': int(self.status), 'result': self.result, 'msg': self.message, 'data': self.data}

try:
    a = ""
    raise ApiException(msg="my excepition is raised ")




except ApiException, e:
    print e.toDict()

