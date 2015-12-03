import socket
import select
import json


class Server(object):

    def __init__(self,host="localhost",port=8888,buffsize=4096):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.buffsize = buffsize
        self.socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.socket.bind((self.host,self.port))
        self.socket.listen(3)
        self.connect = True
