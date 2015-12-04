import threading
import room


class game():
    def __init__(self):
        self.existing_names = set()
        self.username = dict()
        self.last_id_user = 0
        self.rooms = list()
        self.user_room = dict()
        self.last_id_room = 0

    def login(self,player_name):
        if player_name in self.existing_names:
            return -1
        self.existing_names.add(player_name)
        self.last_id_user += 1
        self.user_room[self.last_id_user] = 0
        self.username[self.last_id_user] = player_name
        return self.last_id_user

    def logout(self,userid):
        self.leaveRoom(userid)
        if userid in self.username:
            del self.user_room[userid]
            uname = self.username[userid]
            del self.username[userid]
            if uname in self.existing_names:
                self.existing_names.remove(uname)
            return 1

    def createRoom(self, userid, room_name):
        self.last_id_room += 1
        self.rooms.append(room.room(self.last_id_room, room_name))
        self.joinRoom(userid,self.last_id_room)
        return self.last_id_room


    def joinRoom(self,userid,room_id):
        if (userid not in self.username):
            return -1
        self.user_room[userid] = room_id
        self.rooms[room_id-1].addPlayer(userid)
        return 1

    def leaveRoom(self, userid):
        if (userid not in self.username):
            return -1
        room_id = self.user_room[userid]
        del self.user_room[userid]
        self.rooms[room_id-1].users.remove(userid)
        if len(self.rooms[room_id-1].users) == 0:
            del self.rooms[room_id-1]
        return 1

