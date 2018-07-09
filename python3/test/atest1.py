# encoding:utf-8
# usr/bin/python
from socketserver import StreamRequestHandler, TCPServer


class EchoHandler(StreamRequestHandler):
    # ack is added keyword-only argument. *args, **kwargs are
    # any normal parameters supplied (which are passed on)
    def __init__(self, ack, *args, **kwargs):
        self.ack = ack
        super(EchoHandler, self).__init__(*args, **kwargs)

    def handle(self):
        for line in self.rfile:
            self.wfile.write(self.ack + line)

serv = TCPServer(('', 15000), EchoHandler)
serv.serve_forever()