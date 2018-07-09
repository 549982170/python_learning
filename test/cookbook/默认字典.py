#!/usr/bin/env python
# encoding:utf8
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print d
d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print d

a = {}
# setdefault  -- 键不存在时，设置的默认键值,存在则不修改
a.setdefault("s", "ss")
print a['s']
