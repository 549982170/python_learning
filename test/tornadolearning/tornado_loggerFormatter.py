# -.- coding:utf-8 -.-
# __author__ = 'zhengtong'
import tornado.ioloop
import tornado.web
import tornado.options
import tornado.httpserver
import tornado.concurrent
import tornado.log
import logging
import os


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            ('/', DemoHandler),
        ]

        self.settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            cookie_secret='MEZzzzzzl4NkRWFtb3zzzzg3Y1JMZm5IMnBDcZEXOVhCNXNzzzzRWXJ6ax2d0pzzzz=',
            xsrf_cookies=True,
            compress_response=True,
            login_url='/',
        )
        super(Application, self).__init__(handlers, **self.settings)


class DemoHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('hello world!')


class LogFormatter(tornado.log.LogFormatter):
    def __init__(self):
        super(LogFormatter, self).__init__(
            fmt='%(color)s[%(asctime)s %(filename)s:%(funcName)s:%(lineno)d %(levelname)s]%(end_color)s %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )


def main():
    tornado.options.define("port", default=5004, help="run on the given port", type=int)
    tornado.options.parse_command_line()
    [i.setFormatter(LogFormatter()) for i in logging.getLogger().handlers]
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
