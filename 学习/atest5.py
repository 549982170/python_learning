# coding:utf-8
# !/user/bin/python
"""
自动化脚本脚本
2.X版本改动真大啊"-.-"！
注意:执行带下划线的任务需要变成"-",
例:fab -H 112.74.186.24 pull-svr-code restart-generator-svr
"""
from fabric import task
from fabric import Connection

key_filename = "./Identity"
host = "112.74.186.24"
user = "developer"
port = 22


def update_config(connect):
    run_host = connect.host if connect.host.split(".").__len__() == 4 else host  # 默认测试服
    conf = {
        "host": run_host,
        "user": user,
        "port": port,
        "connect_kwargs": {"key_filename": key_filename},
    }
    for k, v in conf.items():
        if hasattr(connect, k):
            setattr(connect, k, v)
    return connect


@task
def pull_svr_code(connect_obj):
    """拉取代码
    """
    with update_config(connect_obj) as c:
        with c.cd("/data/develop/generator/generator"):
            c.run('git pull', warn=True, pty=False)


@task
def restart_generator_svr(connect_obj):
    """重启服务器
    """
    with update_config(connect_obj) as c:
        with c.cd("/data/develop/generator/deploy"):
            c.run('./supervisor_ctl.sh restart generator', warn=True, pty=False)
            ret = c.run('./supervisor_ctl.sh status |grep generator', warn=True, pty=False)
            stdout = ret.stdout
            status = stdout.split()
            if status[1] == "RUNNING":
                print(u"%s重启成功" % status[0])


@task
def restart_all_svr(connect_obj):
    """重启所有服务
    """
    with update_config(connect_obj) as c:
        with c.cd("/data/develop/generator/deploy"):
            c.run('git pull', warn=True, pty=False)
            c.run('./supervisor_ctl.sh restart all', warn=True, pty=False)
            ret = c.run('./supervisor_ctl.sh status', warn=True, pty=False)
            stdout = ret.stdout
            status_list = stdout.split("\n")
            for ca in status_list:
                status = ca.split()
                if not status:
                    continue
                if status[1] == "RUNNING":
                    print(u"%s重启成功" % status[0])
                else:
                    print(u"%s重启失败" % status[0])
                    break


@task
def rsync_db(connect_obj):
    """同步结构"""
    with update_config(connect_obj) as c:
        with c.cd("/data/develop/generator/generator"):
            c.run('workon developgenerator && python manage.py migrate', warn=True, pty=False)


if __name__ == '__main__':
    server = Connection(host=host)
    pull_svr_code(server)
    restart_generator_svr(server)
