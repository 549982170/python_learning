#!/usr/bin/env python
#coding=utf-8

__author__ = 'shi.xiaolong'

import os
import sys
import git
import time
import ConfigParser
import subprocess
import logging
import getpass
import hashlib
import pexpect
import types
import shutil
import traceback

#from log import initLogging
#initLogging('log/output.log')

#code path
_code_moxian_m1 = os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__), 'code_moxian_m1'), 'moxian_m1'))
_code_moxian_outsource = os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__), 'code_moxian_outsource'), 'moxian_outsource'))
_code_moxian_m2 = os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__), 'code_moxian_m1'), 'moxian_m1_master_m2/moxian_m1'))
_log_file = os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__),'log'),'output.log'))
_work_path = os.path.abspath(os.path.dirname(__file__))

_CFG_PATH = os.path.normpath(os.path.join(os.path.dirname(__file__),'setting.py'))
cf = ConfigParser.ConfigParser()

cf.read(_CFG_PATH)
sections = cf.sections()
_MODULE_NAME = dict()
for index,key in enumerate(sections):
    _MODULE_NAME[index] = key
_MODULE_NAME[0] = 'START_ALL'
_MODULE_NAME[len(sections)] = 'Exit'

#ssh password.
_SSHPWD = cf.get('config','sshpwd')

#mocule code in outsource git
_module_out = ["mo_pal","mo_moment"]

#module in master_m2
_module_master_m2 = ["mo_deploy","mo_shake","mo_activities","mo_game","mo_game","mo_report","mo_vas","mo_common_permission"]

#switching path
def switchpath(module):
    if module in _module_out:
        os.chdir(_code_moxian_outsource)
        os.chdir("%s" % module)
    elif module in _module_master_m2:
        os.chdir(_code_moxian_m2)
        os.chdir("%s" % module)
    else:
        os.chdir(_code_moxian_m1)
        if module == 'mo_shop_moment':
            os.chdir('mo_moment')
        else:
            os.chdir("%s" % module)

#copy file
class Move(object):
    def __init__(self, i):
        self.module = switchmodule(i)
    
    @property
    def copy(self):
        module = self.module
        if type(module) == types.StringType:
            switchpath(module)
            os.chdir('build/libs')
            srcfile = os.path.join(os.getcwd(),os.listdir(os.getcwd())[0])
            destpath = os.path.join(_work_path, 'onlinepkg')
            pkg_time = time.strftime("%Y_%m_%d_%H_%M", time.localtime())
            destpath = os.path.join(destpath,pkg_time)
            os.mkdir(destpath)
            shutil.copy2(srcfile, destpath)
            print '>>>>> BackUp %s file finished!' % module
        elif type(module) == types.ListType:
            pkg_time = time.strftime("%Y_%m_%d_%H_%M", time.localtime())
            destpath = os.path.join(_work_path, 'onlinepkg')
            destpath = os.path.join(destpath,pkg_time)
            os.mkdir(destpath)
            for m in module:
                switchpath(m)
                os.chdir('build/libs')
                srcfile = os.path.join(os.getcwd(),os.listdir(os.getcwd())[0])
                shutil.copy2(srcfile, destpath)
                print '>>>>> BackUp %s file finished!' % m
            
#switch module
def switchmodule(i):
    if i.isdigit():
        module = _MODULE_NAME[int(i)]
        if i == '0':
            module = _MODULE_NAME.values()[1:-1]
    else:
        modulelist = []
        for k in i.split(','):
            module = _MODULE_NAME[int(k)]
            modulelist.append(module)
        module = modulelist
    return module

#pull code from git
class GIT(object):
    def __init__(self):
        self.gituser = cf.get('config','gituser')
        self.gitpwd = cf.get('config','gitpass')
        self.gitip = cf.get('config','gitip')
        self.gitport = cf.get('config','gitport')
    def gitinit(self):
        command = "https://{gituser}@{gitip}:@gitport/r/moxian_m1.git".format(gituser=self.gituser,gitip=self.gitip,gitport=self.gitport)
        git.Git().clone(command)
    
    @property
    def gitpull(self):
        os.chdir(_code_moxian_m1)
        self._pull()
        os.chdir(_code_moxian_outsource)
        self._pull()
        os.chdir(_code_moxian_m2)
        self._pull()
    def _pull(self):
        try:
            child = pexpect.spawn('git pull')
            child.logfile = None
            child.expect('^Password.*')
            child.sendline(self.gitpwd)
            #child.expect(".*")
            child.interact()
        except OSError:
            os.popen("echo '------------%s Exit at %s------------' >> %s 2>&1" % (USER,time.strftime("%Y_%m_%d_%H_%M", time.localtime()),_log_file))
            sys.exit()
                
#compile package use gradle
class Compile(object):
    def __init__(self,i):
        self.module = switchmodule(i)
    @property
    def gradle(self):
        module = self.module
        if type(module) == types.StringType:
            switchpath(module)
            print ">>>>>%s Module compileing...,please wait" % module
            #os.popen("gradle clean war >> ../../../log/output.log 2>&1")
            os.popen("gradle clean war >> %s 2>&1" % _log_file)
            if os.path.exists("build/libs/%s.war" % module):
                print ">>>>>%s Module,Build Success." % module
            else:
                print ">>>>>%s Module,Build Failed!" % module
                os.popen("echo '------------%s Exit at %s------------' >> %s 2>&1" % (USER,time.strftime("%Y_%m_%d_%H_%M", time.localtime()),_log_file))
                sys.exit(1)
        elif type(module) == types.ListType:
            for m in module:
                switchpath(m) 
                print ">>>>>%s Module compileing...,please wait" % m
                #os.popen("gradle clean war >> ../../../log/output.log 2>&1")
                os.popen("gradle clean war >> %s 2>&1" % _log_file)
                if os.path.exists("build/libs/%s.war" % m):
                    print ">>>>>%s Module,Build Success." % m
                else:
                    print ">>>>>%s Module,Build Failed!" % m
                                    
#scp upload file
class SCP(object):
    def __init__(self,i):
        self.module = switchmodule(i)
    
    @property
    def scpsend(self):
        module = self.module
        if type(module) == types.StringType:
            scpip = cf.get(module,'IP')
            scpport = cf.get(module,'Port')
            scppath = cf.get(module,'Root_Respostiory_Path')
            switchpath(module)
            os.chdir('build/libs')
            try:
                modulewar = self.module+'.war'
                CMD = "scp -P {scpport} {warpackage} root@{scpip}:{scppath}/new".format(scpport=scpport, warpackage=modulewar, scpip=scpip, scppath=scppath)
                child = pexpect.spawn(CMD)
                child.expect('.*assword:')
                child.sendline(_SSHPWD)
                child.expect('%s.war.*' % module)
                child.interact()
            except Exception, e:
                traceback.print_exc()
                print '>>>>>%s SCP FAILED！' % module
                os.popen("echo '------------%s Exit at %s------------' >> %s 2>&1" % (USER,time.strftime("%Y_%m_%d_%H_%M", time.localtime()),_log_file))
                sys.exit(1)
            else:
                print ">>>>>%s SCP Success" % module
        elif type(module) == types.ListType:
            for m in module:
                scpip = cf.get(m,'IP')
                scpport = cf.get(m,'Port')
                scppath = cf.get(m,'Root_Respostiory_Path')
                try:
                    switchpath(m)
                    os.chdir('build/libs')
                    modulewar = m +'.war'
                    CMD = "scp -P {scpport} {warpackage} root@{scpip}:{scppath}/new".format(scpport=scpport, warpackage=modulewar, scpip=scpip, scppath=scppath)
                    child = pexpect.spawn(CMD)
                    child.expect('.*assword:')
                    child.sendline(_SSHPWD)
                    child.expect('%s.war.*' % module)
                    child.interact()
                except Exception, e:
                    traceback.print_exc()
                    print '>>>>> %s SCP FAILED！' % m
                    child.close()
                else:
                    print '>>>>> %s SCP Success' % m
    
#make a new directory for .war package
class MkDir(object):
    def __init__(self,i):
        self.module = switchmodule(i)
    
    @property
    def new(self):
        module = self.module
        if type(module) == types.StringType:
            sship = cf.get(module,'IP')
            sshport = cf.get(module,'Port')
            sshpath = cf.get(module,'Root_Respostiory_Path')
            try:
                CMD = "ssh -p {sshport} {sship}".format(sshport=sshport,sship=sship)
                child = pexpect.spawn(CMD)
                child.expect('.*assword:')
                child.sendline(_SSHPWD)
                child.expect('.*')
                CMD1 = "cd {path}".format(path=sshpath)
                child.sendline(CMD1)
                child.expect('.*')
                child.sendline('mkdir new')
                child.expect('.*')
                child.sendline("exit")
                child.expect(".*")
                child.interact() 
            except Exception, e:
                traceback.print_exc()
                child.close()
                print '>>>>> Mkdir new FAILED！'
            else:
                print '>>>>> Mkdir new Success.'
        elif type(module) == types.ListType:
            for m in module:
                sship = cf.get(m,'IP')
                sshport = cf.get(m,'Port')
                sshpath = cf.get(m,'Root_Respostiory_Path')
                try:
                    CMD = "ssh -p {sshport} {sship}".format(sshport=sshport,sship=sship)
                    child = pexpect.spawn(CMD)
                    child.expect('.*assword:')
                    child.sendline(_SSHPWD)
                    child.expect('.*')
                    CMD1 = "cd {path}".format(path=sshpath)
                    child.sendline(CMD1)
                    child.expect('.*')
                    child.sendline('mkdir new')
                    child.expect('.*')
                    child.sendline("exit")
                    child.expect(".*")
                    child.interact() 
                except Exception, e:
                    traceback.print_exc()
                    child.close()
                    print '>>>>> Mkdir new FAILED！'
                else:
                    print '>>>>> Mkdir new Success.'

#restart tomcat
class TomCat(object):
    def __init__(self,i):
        self.module = switchmodule(i)
    
    @property
    def restart(self):
        module = self.module
        if type(module) == types.StringType:
            scpip = cf.get(module,'IP')
            scpport = cf.get(module,'Port')
            scppath = cf.get(module,'Root_Respostiory_Path')
            os.chdir(_work_path)
            try:
                #scp
                CMD = "scp -P {scpport} tomcat.sh root@{scpip}:{scppath}".format(scpport=scpport, scpip=scpip, scppath=scppath)
                child = pexpect.spawn(CMD)
                child.expect('.*assword:')
                child.sendline(_SSHPWD)
                child.interact()
                #ssh login
                CMD1 = "ssh -p {sshport} {sship}".format(sshport=scpport,sship=scpip)
                child1 = pexpect.spawn(CMD1)
                child1.expect('.*assword:')
                child1.sendline(_SSHPWD)
                child1.expect('.*')
                CMD2 = 'cd {path}'.format(path=scppath)
                child1.sendline(CMD2)
                child1.expect('.*')
                child1.logfile = sys.stdout
                CMD3 = './tomcat.sh %s' %  module
                child1.sendline(CMD3)
                child1.expect('.*')
                #child1.sendline('rm -rf tomcat.sh')
                #child1.expect('.*')
                child1.logfile = None
                child1.sendline("exit")
                child1.expect("logout.*")
                child1.interact()
            except Exception, e:
                traceback.print_exc()
                print '>>>>>restart tomcat.sh FAILED！'
                child.close()
                child1.close()
                os.popen("echo '------------%s Exit at %s------------' >> %s 2>&1" % (USER,time.strftime("%Y_%m_%d_%H_%M", time.localtime()),_log_file))
                sys.exit()
            else:
                print '>>>>>restart tomcat.sh Success'
                
        elif type(module) == types.ListType:
            for m in module:
                scpip = cf.get(m,'IP')
                scpport = cf.get(m,'Port')
                scppath = cf.get(m,'Root_Respostiory_Path')
                os.chdir(_work_path)
                try:
                    #scp
                    CMD = "scp -P {scpport} tomcat.sh root@{scpip}:{scppath}".format(scpport=scpport, scpip=scpip, scppath=scppath)
                    child = pexpect.spawn(CMD)
                    child.expect('.*assword:')
                    child.sendline(_SSHPWD)
                    #child.expect('tomcat.sh.*')
                    child.interact()
                    #ssh login
                    CMD1 = "ssh -p {sshport} {sship}".format(sshport=scpport,sship=scpip)
                    child1 = pexpect.spawn(CMD1)
                    child1.expect('.*assword:')
                    child1.sendline(_SSHPWD)
                    child1.expect('.*')
                    CMD2 = 'cd {path}'.format(path=scppath)
                    child1.sendline(CMD2)
                    child1.expect('.*')
                    child1.logfile = sys.stdout
                    CMD3 = './tomcat.sh %s' %  m
                    child1.sendline(CMD3)
                    child1.expect('.*')
                    child1.logfile = None
                    #child1.sendline('rm -rf tomcat.sh')
                    #child1.expect('.*')
                    child1.sendline("exit")
                    child1.expect("logout.*")
                    child1.interact()
                except Exception, e:
                    traceback.print_exc()
                    print '>>>>>restart tomcat.sh FAILED！'
                    child.close()
                    child1.close()
                else:
                    print '>>>>>restart tomcat.sh Success'
        
#run interface test
class InterFace():
    def __init__(self,i):
        self.module = switchmodule(i)
    def test(self):
        module = self.module
        if type(module) == types.StringType:
            #/data/moxian_package/code/moxian_m1/mo_ad/build/libs
            print os.getcwd()
            os.chdir('../../../../../apitest/InterFaceAutoTest/testcase/')
            print os.getcwd()
            CMD = "%s.py"
            os.system("")
            os.popen("echo '------------%s Exit at %s------------' >> %s 2>&1" % (USER,time.strftime("%Y_%m_%d_%H_%M", time.localtime()),_log_file))
            sys.exit()
            
#user limit
USER = ''
def userlogin():
    print "###################################################################"
    print "########        Moxian_Package(login)                      ########"
    print "###################################################################"
    print "Please Input your username"
    global USER
    USER = raw_input("login as:")
    if USER not in eval(cf.get('config','user')):
        print 'Access denied'
        return False
    #判断是否存在此用户
    opts = cf.options("config")
    if USER not in opts:
        pwd_old = getpass.getpass(prompt='Firsrt Login,please set your password: ')
        pwd_new = getpass.getpass(prompt='Input again:')
        if not any([pwd_old,pwd_new]):
            print '>>>>>password cannot be Null'
            sys.exit()
        if pwd_old != pwd_new:
            print '>>>>>passowrd not equals.'
            sys.exit()
        else:
            md5_pwd = hashlib.md5(str(pwd_new)).hexdigest()
            cf.set('config', USER, md5_pwd)
            cf.write(open(_CFG_PATH, "w"))
            os.popen("echo '------------%s login Successfully at %s------------' >> %s 2>&1" % (USER,time.strftime("%Y_%m_%d_%H_%M", time.localtime()),_log_file))
            return True
        
    else:
        for i in range(3):
            pwd = getpass.getpass(prompt='Please input your password to log: ')
            if hashlib.md5(str(pwd)).hexdigest() == cf.get('config', USER):
                os.popen("echo '------------%s login Successfully at %s------------' >> %s 2>&1" % (USER,time.strftime("%Y_%m_%d_%H_%M", time.localtime()),_log_file))
                return True
            if i != 2:
                print "Wrong password,please input agine. You have %d time left" % (2-i)
            else:
                print "Sorry,You've tried 3 times." 
        print 'Login failed!!!'
        return False
#use cn default
ENV = 1

def env_select():
    print "#####################################################################"
    print "########        Moxian_Package(ENV_SELECT)                   ########"
    print "#####################################################################"
    print "Please choose the Environment(One Limited)"
    print "1.CN (Test environment.)"
    print "2.Online (Oline environemnt)"
    print "3.Exit"
    global ENV
    ENV = raw_input(">>>>>Please Choose:")
    if not ENV in ['1', '2','3']:
        print '>>>>> Wrong Input!'
        os.popen("echo '------------%s Exit at %s------------' >> %s 2>&1" % (USER,time.strftime("%Y_%m_%d_%H_%M", time.localtime()),_log_file))
        print '>>>>> Exit.'
        sys.exit()
    elif ENV == '3':
        os.popen("echo '------------%s Exit at %s------------' >> %s 2>&1" % (USER,time.strftime("%Y_%m_%d_%H_%M", time.localtime()),_log_file))
        print '>>>>> Exit.'
        sys.exit()
    return True 

#main function  
def main():
    n = userlogin()
    if not n:
        sys.exit()
    #e = env_select()
    #if not e:
    #    sys.exit()
    while 1:
        print "###################################################################"
        print "########            Moxian_Package(send)                   ########"
        print "###################################################################"
        print "Please choose the module(If you have multiple-choice,Separated by ,).\n"
        for key in _MODULE_NAME.keys():
            print "{a}.{b}".format(a=key,b=_MODULE_NAME[key])
        i = raw_input(">>>>>Please Choose:")
        if not i:
            continue
        #多选
        if len(i.split(',')) > 1:
            i = i.split(',')
            flag = '2'
        #单选
        elif i.isdigit():
            flag = '1'
            if not int(i) in _MODULE_NAME.keys():
                logging.error("Your choose is %d !!" % int(i))
                continue
            elif _MODULE_NAME[int(i)] == "Exit":
                print '>>>>>Exit.'
                os.popen("echo '------------%s Exit at %s------------' >> %s 2>&1" % (USER,time.strftime("%Y_%m_%d_%H_%M", time.localtime()),_log_file))
                sys.exit()
        if flag == '1':
            logging.info("Your choose is %d-%s" % (int(i),_MODULE_NAME[int(i)]))
            print ">>>>>Your choose is %s-%s\n" % (str(i),_MODULE_NAME[int(i)])
        elif flag == '2':
            i = ','.join(i)
            logging.info("Your choose is %s" % (i))
            print ">>>>>Your choose is %s" % (i)
        print ">>>>>1.I'm SURE."
        print ">>>>>2.Back to MainMenu."
        j = int(raw_input(">>>>>Please choose:\n"))
        if j == 2:
            continue
        elif j == 1:
            print '--------------BEGINE-----------------'
            break
        else:
            print '>>>>>Wrong Number!'
            time.sleep(2)
            continue
    
    git = GIT()
    git.gitpull
    compile = Compile(i)
    compile.gradle
    move = Move(i)
    move.copy
    mkdir = MkDir(i)
    mkdir.new
    scp = SCP(i)
    scp.scpsend 
    tomcat = TomCat(i)
    tomcat.restart
    '''
    if int(ENV) == 2:
        move = Move(i)
        move.copy
    else:
        mkdir = MkDir(i)
        mkdir.new
        scp = SCP(i)
        scp.scpsend 
        tomcat = TomCat(i)
        tomcat.restart
    '''
    
    #api = InterFace(i)
    #api.test()
    
if __name__ == '__main__':
    if len(sys.argv) == 1:
         main()
