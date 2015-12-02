import socket
import select
import json


class Server(object):

    def __init__(self,host="localhost",port=8888,buffsize=4096):
        super(Server, self).__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.buffsize = buffsize
        self.socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.socket.bind((self.host,self.port))
        self.socket.listen(3)
        self.connect = True


    def send(self,msg):
        if self.connect:
            try:
                _, ready_to_write, _ = select.select([],[self.socket],[])
                if self.socket in ready_to_write:
                    self.socket.sendall(msg.encode())
            except select.error:
                self.close


    def recv(self):
        if self.connect:
            try:
                ready_to_read, _, _ = select.select([self.socket], [], [], 0.6)
                if self.socket in ready_to_read:
                    return self.socket.recv(self.buffsize)
            except select.error:
                self.close


    def close(self):
        try:
            self.connect = False
            self.socket.shutdown(socket.SHUT_RDWR)
            self.socket.close()
        except OSError:
            pass

"""
a = Server()

while True:
    sock, addr = a.socket.accept()
    print("koneksi pada",addr)
    str = json.loads(sock.recv(1024).decode("UTF-8"))
    x = str[0]
    y = str[1]
    print(x, " dan ", y)
    if str is not None:
        sock.close()
        break
"""