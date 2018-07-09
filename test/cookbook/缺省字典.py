#!/usr/bin/python
# coding: UTF-8
import collections
import json

m = collections.defaultdict(int)
print m

m = collections.defaultdict(str)
print m

m = collections.defaultdict(lambda: '[default value]')
print m['s']

# 用缺省字典表示简单的树
tree = lambda: collections.defaultdict(tree)
root = tree()
root['menu']['id'] = 'file'
root['menu']['value'] = 'File'
root['menu']['menuitems']['new']['value'] = 'New'
root['menu']['menuitems']['new']['onclick'] = 'new();'
root['menu']['menuitems']['open']['value'] = 'Open'
root['menu']['menuitems']['open']['onclick'] = 'open();'
root['menu']['menuitems']['close']['value'] = 'Close'
root['menu']['menuitems']['close']['onclick'] = 'close();'
print json.dumps(root, sort_keys=True, indent=4, separators=(',', ': '))
