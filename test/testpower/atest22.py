#!user/bin/python
# encoding:utf-8

def processor(page, maxmun, num=1, count=0):
    count += page
    if count <= maxmun:
        yield num
    else:
        count = 0
        num += 1
        yield num


c = processor(1, 2)
print c.next()
c = processor(2, 2)
print c.next()
c = processor(2, 2)
print c.next()

#
# for ca in processor(1, 2):
#     print ca
