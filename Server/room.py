from Gameplay import Board
from string import ascii_lowercase

class room():
    global pion
    pion = list(ascii_lowercase)

    def __init__(self, room_id, room_name):
        self.rid = room_id
        self.rname = room_name
        self.users = list()
        self.board = Board.Board()

    def addPlayer(self, userid):
        self.users.append(userid)
        self.board.addPlayer(userid,pion[len(self.users)-1])