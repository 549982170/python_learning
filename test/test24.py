#!user/bin/python
# encoding:utf-8

def test():
    msg = '1'
    try:
        return msg
    finally:
        print 'finally...'
        msg = '2'


print test()
