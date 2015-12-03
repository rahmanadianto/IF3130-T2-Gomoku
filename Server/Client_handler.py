import socket
import select
import json
import game
import Server

class Client_handler(object):

    def __init__(self,game,socket,addr):
        self.game = game
        self.socket = socket
        self.addr = addr
        self.buffsize = 4096
        self.connect = True

        self.id = -1
        self.room_id = -1
        self.uname = ""


    def send(self,msg):
        if self.connect:
            try:
                _, ready_to_write, _ = select.select([],[self.socket],[])
                if self.socket in ready_to_write:
                    msg = json.dumps(msg)
                    self.socket.sendall(msg.encode())
            except select.error:
                self.close


    def recv(self):
        if self.connect:
            try:
                ready_to_read, _, _ = select.select([self.socket], [], [], 0.6)
                if self.socket in ready_to_read:
                    msg = self.socket.recv(self.buffsize)
                    if len(msg)==0:
                        self.close()

                    self.recv_msg(msg)
            except select.error:
                self.close

    def recv_msg(self,msg):
        msg = json.loads(msg.decode("UTF-8"))
        msg_send = list()
        if "login" in msg:
            msg = msg.split("login")
            for message in msg:
                self.game = game.game()
                username = message
                #print(message)
                userid = self.game.login(username)
            if userid > 0:
                self.id = userid
                self.uname = username
                msg_send.append(1)
                msg_send.append(userid)
            else:
                msg_send.append(0)
            self.send(msg_send)
        elif "createroom" in msg:
            msg = msg.split("createroom")
            for message in msg:
                room_name = message
                roomid = self.game.createRoom(self.id,room_name)
                #print("***",message,"***")
            if roomid > 0:
                self.room_id = roomid
                msg_send.append(1)
                msg_send.append(roomid)
            else:
                msg_send.append(0)
            self.send(msg_send)




    def close(self):
        try:
            self.connect = False
            self.socket.shutdown(socket.SHUT_RDWR)
            self.socket.close()
        except OSError:
            pass

a = Server.Server()
while True:
    handler, addr = a.socket.accept()
    CL = Client_handler(game.game,handler,addr)
    print("koneksi pada",addr)
    CL.recv()
    print("added username: ",CL.uname," dengan id =",CL.id)
    print("Username yang sedang online:",CL.game.existing_names)
    CL.recv()
    print("added room: ",CL.game.rooms[1].rname," dengan id =",CL.room_id)
    for a in CL.game.rooms:
        print("Daftar room: ",a.rname)
    if str is not None:
        CL.close()
        break
