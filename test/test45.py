#coding:utf-8
import urllib
import urlparse


def url_add_params(url, **params):
    """ 在网址中加入新参数 """
    pr = urlparse.urlparse(url)
    query = dict(urlparse.parse_qsl(pr.query))
    query.update(params)
    prlist = list(pr)
    prlist[4] = urllib.urlencode(query)
    return urlparse.ParseResult(*prlist).geturl()


if __name__ == "__main__":
    url = 'http://www.google.com'
    print url_add_params(url, token=123, site="bbs")
