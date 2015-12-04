import socket
import select
import json
import game
import room
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
        if msg['type'] == "login":
            message = msg['name']
            username = message
            #print(message)
            userid = self.game.login(username)
            if userid > 0:

                self.id = userid
                self.uname = username
                msg_send = '{"type":"login","state":"success", "user_id":"'+str(self.id)+'"}'
            else:
                msq_send = '{"type":"login","state":"failed", "user_id":"'+str(self.id)+'"}'
            self.send(msg_send)
        elif msg['type'] == "create_room":
            message = msg['room_name']
            room_name = message
            roomid = self.game.createRoom(self.id,room_name)
            #print("***",message,"***")
            if roomid > 0:
                self.room_id = roomid
                msg_send = '{"type":"create_room","state":"success", "room_id":"'+str(self.room_id)+'"}'
            else:
                msg_send = '{"type":"create_room","state":"failed", "room_id":"'+str(self.room_id)+'"}'
            self.send(msg_send)
        elif msg['type'] == "join_room":
            roomid = int(msg['room_id'])
            success = self.game.joinRoom(self.id,roomid)
            #print("***",message,"***")
            if success > 0:
                self.room_id = roomid
                msg_send = '{"type":"join_room","state":"success", "room_id":"'+str(self.room_id)+'"}'
            else:
                msg_send = '{"type":"join_room","state":"failed", "room_id":"'+str(self.room_id)+'"}'
            self.send(msg_send)
        elif msg['type'] == "leave_room":
            userid = int(msg['user_id'])
            success = self.game.leaveRoom(userid)
            #print("***",message,"***")
            if success > 0:
                self.room_id = -1
                msg_send = '{"type":"leave_room","state":"success", "room_id":"'+str(self.room_id)+'"}'
            else:
                msg_send = '{"type":"leave_room","state":"failed", "room_id":"'+str(self.room_id)+'"}'
            self.send(msg_send)
        elif msg['type'] == "logout":
            userid = int(msg['user_id'])
            success = self.game.logout(userid)
            #print("***",message,"***")
            if success > 0:
                del self
                self.close()
            else:
                msg_send = '{"type":"logout","state":"failed", "room_id":"'+str(self.room_id)+'"}'
            self.send(msg_send)




    def close(self):
        try:
            self.connect = False
            self.socket.shutdown(socket.SHUT_RDWR)
            self.socket.close()
        except OSError:
            pass

    def __del__(self):
        print ("User " + self.uname+ " dengan id " + str(self.id) + " logout")


a = Server.Server()
game = game.game()
while True:
    handler, addr = a.socket.accept()
    CL = Client_handler(game,handler,addr)
    print("koneksi pada",addr)
    CL.recv()
    print("added username: ",CL.uname," dengan id =",CL.id)
    print("Username yang sedang online:",CL.game.existing_names)
    CL.game.rooms.append(room.room(1, "haiiii"))
    CL.game.last_id_room += 1
    CL.recv()
    print("joined room: ",CL.game.rooms[CL.room_id-1].rname," dengan id =",CL.room_id)
    for a in CL.game.rooms:
        print("Daftar room: ",a.rname)
    CL.recv()
    if(len(CL.game.rooms)>0):
        for a in CL.game.rooms:
            print("Daftar room: ",a.rname)
    else:
        print("tidak ada room")

    CL.recv()
