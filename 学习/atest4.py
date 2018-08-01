# coding:utf-8
# !/user/bin/python
import logging
from threading import Timer


logger = logging.getLogger('debug')
rankTimer = None


def timer_delete_handler():
    """定时清理失效handler"""
    try:
        logger.info('Clean user handler memory start...')

        a = "s"
        print(int(a))
    except Exception as e:
        logger.exception(e)
    finally:
        global rankTimer
        logger.info('Clean user handler memory end...')
        rankTimer = Timer(SECONDS, 1)  # 60秒
        rankTimer.start()
