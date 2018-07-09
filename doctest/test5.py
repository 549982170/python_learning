# coding:utf-8
# !/user/bin/python
import subprocess
import tempfile


def chang2txtbyantiword(fpath, tpath):
    """通过antiword读取doc,需要安装antiword,目前仅用于linux(详情见:http://www.winfield.demon.nl)
    wget http://www.winfield.demon.nl/linux/antiword-0.37.tar.gz
    tar -xvf antiword-0.37.tar.gz
    cd antiword-0.37
    make && make install 
    @param fp: 相对文件路径"""
    try:
        com = "antiword -m UTF-8.txt -t " + fpath + " > " + tpath
        out_temp = tempfile.SpooledTemporaryFile(bufsize=10 * 1000)
        fileno = out_temp.fileno()
        obj = subprocess.Popen(com, shell=True, stdout=fileno, stderr=fileno)
        output = obj.wait()
        out_temp.seek(0)
        lines = out_temp.readlines()

        if output == 0:  # 执行成功
            return True
        return False
    except:
        return False
    finally:
        if out_temp:
            out_temp.close()


a = "/data/appsystems/appSvr00/media/upload/doc/20170510/71d60eb8-3564-11e7-995c-000c29eb773f.doc"
b = "/data/appsystems/appSvr00/media/upload/txt/20170510/71d60eb8-3564-11e7-995c-000c29eb773f.txt"
chang2txtbyantiword(a, b)
