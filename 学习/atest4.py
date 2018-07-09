# coding:utf-8
# !/user/bin/python
'''
Created on 2017年3月22日
@author: yizhiwu
自动化脚本
'''

from fabric.api import *
from fabric.colors import *
from fabric.context_managers import *

host = '111.230.177.230'
user = 'appuser'

key_filename = "./id_rsa"


def ls_path():
    with settings(host_string=host, key_filename=key_filename, user=user, warn_only=True):
        with cd('/'):
            run('ls -l')


if __name__ == '__main__':
    ls_path()
