import socket
import select

class Connection(object):
    def __init__(self,host="localhost",port=8888,buffsize=4096):
        super(Connection, self).__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.buffsize = buffsize
        self.socket.connect((self.host,self.port))
        self.socket.setblocking(0)
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
        recv_msg = ""
        if self.connect:
            try:
                ready_to_read, _, _ = select.select([self.socket], [], [], 0.6)
                if self.socket in ready_to_read:
                    recv_msg = self.socket.recv(self.buffsize)
            except select.error:
                self.close
        return recv_msg

    def close(self):
        try:
            self.connect = False
            self.socket.shutdown(socket.SHUT_RDWR)
            self.socket.close()
        except OSError:
            pass
