#!/usr/bin/env python
# encoding:utf8

a = ["1", "s", "dd", "ssa"]
b = '\n'.join(str(index) if index % 3 == 0 else ca + "-" for index, ca in enumerate(a))
print b
