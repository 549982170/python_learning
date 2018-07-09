#!user/bin/python
# encoding:utf-8

def test():
    try:
        a = {}
        print a['ss']
    except BaseException:
        pass
    except:
        pass
    finally:
        pass


test()
test()
