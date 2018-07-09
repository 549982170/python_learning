#!user/bin/python
# encoding:utf-8
import subprocess
import re
import os
import MySQLdb
import datetime
import shutil
from time import strftime, localtime

# ---------配置信息---------
dbHost = "172.27.0.105"
dbUser = "root"
dbPwd = "175hj34$%yzw"
dbPort = [3456, 8061]  # 数据库实例数
backupPath = "/data/mysqlbck"  # 备份路径


# --------配置信息结束-----------------
def createbackupsql():
    """创建备份"""
    for myport in dbPort:
        connection = MySQLdb.connect(host=dbHost, user=dbUser, port=myport, passwd=dbPwd)  # create the connection
        cursor = connection.cursor()  # get the cursor
        cursor.execute("show databases")  # select the database
        for dbName in cursor:
            dbName = dbName[0]
            # 数据库名称为bzsh_+数字或者"gameadmin"库备份
            if dbName.startswith('bzsh_') and re.findall("\d+", dbName) or dbName == "gameadmin":
                # 创建新服目录文件夹
                curdate = strftime("%Y-%m-%d", localtime())
                tip = getTip(myport)  # 获取类型
                new_path = os.path.join(backupPath, curdate)
                new_path = os.path.join(new_path, tip)
                print new_path
                if not os.path.exists(new_path):
                    os.makedirs(new_path)
                fileName = os.path.join(new_path, dbName + ".sql")
                com = "mysqldump  -h" + dbHost + ' -u' + dbUser + " -p" + dbPwd + " -P" + str(myport) + \
                      " --opt -R --default-character-set=utf8 " + dbName + " >  " + fileName
                p = subprocess.Popen(com, shell=True)
                output = p.wait()
                if output == 0:  # 执行成功
                    print 'Mysqldump ' + dbName + ' success'
                else:
                    print 'Mysqldump ' + dbName + ' fail'


def cleanbackupsql():
    folderList = os.listdir(backupPath)  # 列出目录下的所有目录
    toDate = (datetime.datetime.now()).date()
    for fd in folderList:
        fdDate = datetime.datetime.strptime(fd, "%Y-%m-%d").date()
        if (toDate - fdDate).days >= 7:  # 清除7天前文件目录
            root = os.path.join(backupPath, fd)
            shutil.rmtree(root, True)
            print "Delete the directory 7 days ago success:" + fd


def getTip(port):
    if port == 3456:
        tip = "Android"
    elif port == 8061:
        tip = "IOS"
    else:
        tip = ""
    return tip


if __name__ == '__main__':
    createbackupsql()
    cleanbackupsql()
