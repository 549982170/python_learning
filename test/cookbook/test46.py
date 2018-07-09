#!/usr/bin/python
# coding: UTF-8
import sys, time

def progress(percent, count):
    count = float(count)
    hashes = '#' * int(percent / count * 100)
    spaces = ' ' * (100 - len(hashes))
    sys.stdout.write("\rPercent: [%s] %0.2f%%" % (hashes + spaces, percent/count * 100))
    sys.stdout.flush()
    time.sleep(1)

for i in range(121):
    progress(i, 120)

