class player(object):
    def __init__(self, pid, name, player_addr):
        self.pid = pid
        self.name = name
        self.paddr = player_addr
        self.pion = '-'
        self.roomid = 0

    def getPID(self):
        return self.pid

    def getName(self):
        return self.name

    def getPaddr(self):
        return self.paddr

    def getPion(self):
        return self.pion

    def getRoomid(self):
        return self.roomid

    def setRoomid(self,roomid):
        self.roomid = roomid

    def setPion(self,pion):
        self.pion = pion