from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from datetime import date
import os
import threading


FTP_PORT = 21
FTP_USER = "Waste"
FTP_PASSWORD = "123"
FTP_DIRECTORY = "public"
authorizer = DummyAuthorizer()
authorizer.add_user(FTP_USER, FTP_PASSWORD, FTP_DIRECTORY, perm='elradfmw')

handler = FTPHandler
handler.authorizer = authorizer
handler.banner = "pyftpdlib based ftpd ready."

address = ('', FTP_PORT)
server = FTPServer(address, handler)

server.max_cons = 256
server.max_cons_per_ip = 5

server.serve_forever()
    
