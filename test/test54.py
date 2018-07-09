# coding:utf-8
# !/user/bin/python
items = [{"a": 1, "b": "1"}, {"a": 2, "b": "1A"}, {"a": 3, "b": "1B"}, {"a": 3, "b": "2"}, {"a": 3, "b": "3"},
         {"a": 4, "b": "3B"}, {"a": 5, "b": "3A"}, {"a": 5, "b": "4A"}, {"a": 5, "b": "5A"}, {"a": 5, "b": "6A"}]

b = sorted(items, key=lambda x: (x['A'], x['b'].lower()))
