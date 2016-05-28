#!/usr/bin/env python

# 'hostnamehttpserver.py.'
# Chris Shiels.


import errno
import BaseHTTPServer
import socket
import sys


class HostnameHTTPServer(BaseHTTPServer.HTTPServer):
    def __init__(self,
                 server_address,
                 RequestHandlerClass,
                 bind_and_activate = True):
        BaseHTTPServer.HTTPServer.__init__(self,
                                           server_address,
                                           RequestHandlerClass,
                                           bind_and_activate)

    # Override BaseServer.handle_error() to prevent EPIPE errors.
    def handle_error(self,
                     request,
                     client_address):
        type, value, traceback = sys.exc_info()

        if type == socket.error and value.errno == errno.EPIPE:
            return

        BaseHTTPServer.HTTPServer.handle_error(self,
                                               request,
                                               client_address)


class HostnameHTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            if self.path == "/status":
                self.wfile.write("ok")
            else:
                self.wfile.write(socket.gethostname())
        except socket.error, e:
            if e.errno != errno.ECONNRESET:
                raise
        return

    def do_HEAD(self):
        try:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
        except socket.error, e:
            if e.errno != errno.ECONNRESET:
                raise
        return


class HostnameHTTPServerRunner:
    def go(self, port):
        try:
            print 'Starting HostnameHTTPServer on port %s.' % ( port )
            hostnamehttpserver = HostnameHTTPServer(('', port),
                                                    HostnameHTTPRequestHandler)
            hostnamehttpserver.serve_forever()
        except KeyboardInterrupt:
            hostnamehttpserver.socket.close()
        return 0


sys.exit(HostnameHTTPServerRunner().go(8080))
