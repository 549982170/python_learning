#!/usr/bin/python
# coding: UTF-8
import string
s = '{name} has {n} messages.'
print s.format(name='Guido', n=37)
name = 'Guido'
n = 37
d = '%s has %s messages.' % (name, n)
print d

s = string.Template('$name has $n messages.')
print s.substitute(vars())
