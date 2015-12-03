import threading
from . import room


class game():
    def __init__(self):
        self.existing_names = set()
        self.username = dict()
        self.last_id_user = 0
        self.rooms = list()
        self.last_id_room = 0

    def login(self,player_name):
        if player_name in self.existing_names:
            return -1
        self.existing_names.add(player_name)
        self.last_id_user += 1
        self.username[self.last_id_user] = player_name
        return self.last_id_user

    def logout(self,userid):
        self.leaveRoom(userid)
        if userid in self.username:
            uname = self.username[userid]
            del self.username[userid]
            if uname in self.existing_names:
                self.existing_names.remove(uname)

    def createRoom(self, userid, room_name):
        self.last_id_room += 1
        self.rooms.append(room.room(self.id_room, room_name))
        self.joinRoom(userid,self.last_id_room)
        return self.last_id_room


    def joinRoom(self,userid,room_id):
        if (userid not in self.username) or (room_id not in self.rooms):
            return -1
        self.rooms[room_id].addPlayer(userid)
        return 1

    def leaveRoom(self, userid):
        if (userid not in self.username) or (userid not in self.rooms.users):
            return -1
        roomid = self.rooms[userid].rid
        self.rooms.users.remove(userid)
        if len(self.rooms.users) == 0:
            del self.rooms[roomid]
        return 1

