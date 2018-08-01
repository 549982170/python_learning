#!/usr/bin/python
# encoding:utf-8
import smtplib
from email.mime.text import MIMEText


def send_email(subject, content, to_mail, mime='plain', sender="xxxxx@xxxxx.com", password="xxxxxxx"):
    """

    :param subject: 邮件主题
    :param content: 正文
    :param to_mail: 接收者
    :param mime: 格式
    :param sender:发送者
    :param password: 秘钥
    :return:
    """
    mail_host = 'smtp.kaiheikeji.com'
    msg = MIMEText(content, mime, _charset="UTF-8")
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = to_mail
    s = smtplib.SMTP(host=mail_host, port=587)
    s.login(sender, password)
    s.sendmail(sender, to_mail, msg.as_string())
    s.close()


if __name__ == '__main__':
    subject = u"邮件标题"
    content = u"邮件内容"
    to_mail = u"xxxxxxx@xxxxx.com"
    send_email(subject, content, to_mail)
