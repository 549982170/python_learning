#!/usr/bin/env python
# encoding:utf8

import platform

def isWindowsSystem():
    return 'Windows' in platform.system()

def isLinuxSystem():
    return 'Linux' in platform.system()

print isWindowsSystem()
print isLinuxSystem()