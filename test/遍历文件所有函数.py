#!/usr/bin/env python
# encoding:utf8
from inspect import getmembers, isfunction
import test51
my_filters = {name: function for name, function in getmembers(test51)if isfunction(function)}
print my_filters

