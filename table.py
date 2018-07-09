table = {¡¯Sjoerd¡¯: 4127, ¡¯Jack¡¯: 4098, ¡¯Dcab¡¯: 7678}
>>> for name, phone in table.items():
...
print ¡¯%-10s ==> %10d¡¯ % (name, phone)
for name, phone in table.items():
    print '%-10s ==> %10d' % (name, phone)