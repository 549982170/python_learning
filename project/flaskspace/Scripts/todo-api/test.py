#!/usr/bin/env python

from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse
import json

class GetHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        print self.requestline
        parsed_path = urlparse.urlparse(self.path)
        self.send_response(200)
        self.end_headers()
        
        result = { "result":'true',
                   "code":0,
                   "is_reg":'true',}         
        print parsed_path.query
        
        for item in parsed_path.query.split('&'):
            key, value = item.split('=')
            result[key] = value
            
        print json.dumps(result)   
        self.wfile.write(json.dumps(result))
        return

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('0.0.0.0', 8080), GetHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()
