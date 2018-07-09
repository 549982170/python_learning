#!/usr/bin/python
# coding: UTF-8
import tornado.ioloop
import tornado.web
import json


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        try:
            args = self.request.arguments.get("args")[0]  # get请求的参数
            redata = {"test": "Hello, world", "args": args}  # 返回的数据
            msg = u"sucess"  # 友好提示信息
            data = redata
            self.write(json.dumps(
                {'status': 1, 'result': 1, "data": data, "msg": msg}))  # status和result为1时表示处理成功, result为0时返回友好提示msg
        except Exception as e:
            self.write(json.dumps(
                {'status': 0, 'result': 0, "data": {}, "msg": u"接口错误"}))  # status为0时,表示服务器错误

    def post(self):
        nick = self.get_argument('nick', None)  # POST请求的参数
        self.write("Hello, world")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
