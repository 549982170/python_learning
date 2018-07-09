#!/usr/bin/env python
# encoding:utf8
import time

a = map(str, range(10000000))


def g(n):
    c = 0
    for paragraph in n:
        c += 1
        if c % 2 == 0:
            yield paragraph + '<span class="hh"></span>'
        else:
            yield paragraph

def g2(n):
    txtlist = []
    for index, paragraph in enumerate(n):
        if index % 2 == 0:
            txtlist.append(paragraph)
        else:
            txtlist.append(paragraph + '<span class="hh"></span>')
    return '\n'.join(txtlist)


def g3(n):
    d = map(lambda x: x + '<span class="hh"></span>', n)
    docText = '\n'.join([paragraph for paragraph in d])
    return docText


def g4(n):
    docText = '\n'.join(paragraph for paragraph in n)
    return docText

def g5(n):
    c = '\n'.join(paragraph for paragraph in n)
    # d = '<span class="hh"></span>'.join(paragraph for index, paragraph in enumerate(c) if index % 2 == 0)
    return c

def g6(n):
    docText = '\n'.join(paragraph if index / 2 == 0 else paragraph + '<span class="hh"></span>' for index, paragraph in enumerate(n))
    return docText


t1 = time.time()
docText1 = '\n'.join((g(a)))
t2 = time.time()

t3 = time.time()
docText2 = g2(a)
t4 = time.time()

t5 = time.time()
docText3 = g3(a)
t6 = time.time()

t7 = time.time()
docText4 = g4(a)
t8 = time.time()

t9 = time.time()
docText5 = g5(a)
t10 = time.time()

t11 = time.time()
docText6 = g6(a)
t12 = time.time()

print "g1:", t2 - t1
print "g2:", t4 - t3
print "g3:", t6 - t5
print "g4:", t8 - t7
print "g5:", t10 - t9
print "g6:", t12 - t11



