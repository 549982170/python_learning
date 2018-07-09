#!user/bin/python
# encoding:utf-8
class WidgetShowLazyLoad(object):
    def fetch_complex_attr(self, attrname):
        '''可能是比较耗时的操作， 比如从文件读取'''
        return attrname

    def __getattr__(self, name):
        if name not in self.__dict__:
            self.__dict__[name] = self.fetch_complex_attr(name)
        return self.__dict__[name]


if __name__ == '__main__':
    w = WidgetShowLazyLoad()
    print 'before', w.__dict__
    w.lazy_loaded_attr
    print 'after', w.__dict__
