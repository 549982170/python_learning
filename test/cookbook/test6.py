#!/usr/bin/python
# coding: UTF-8
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

items = [1, 5, 6, 6, 8, 5, 1]
print list(dedupe(items))
