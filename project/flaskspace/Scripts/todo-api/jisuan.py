#!/usr/bin/env python


from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
server = SimpleJSONRPCServer(( 'localhost', 8888, ))
# A well defined API
def add(x, y):
    '''Add x and y'''
    return x + y

def subtract(x, y):
    '''Subtract y from x'''
    return x - y

_EXPOSED = ( add, subtract, )
# register our api
for fn in _EXPOSED:
    server.register_function(fn)
print 'Starting server, use <Ctrl-C> to stop'
server.serve_forever()


