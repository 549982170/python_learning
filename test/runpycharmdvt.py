#!/usr/bin/env python
# encoding:utf8
import subprocess
import traceback


def runcom(_com):
    try:
        p = subprocess.Popen(_com, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, shell=True)
        print "run dvt-jb_licsrv.linux.amd64 suecess"
        p.wait()
    except Exception as e:
        print e
        print traceback.format_exc()


com = "/data/appsystems/pycharm/dvt-jb_licsrv.linux.amd64"

if __name__ == '__main__':
    runcom(com)
