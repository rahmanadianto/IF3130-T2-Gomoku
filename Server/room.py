

class room():
    def __init__(self, room_id, room_name):
        self.rid = room_id
        self.rname = room_name
        self.users = list()

    def addPlayer(self, player):
        self.users.append(player)