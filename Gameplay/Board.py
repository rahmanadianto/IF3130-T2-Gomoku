class Board:
    def __init__(self):
        self.size = 20
        self.playerlist = dict() #default player : 2
        self.board = [[0 for x in range(20)] for x in range(20)]
        self.win = False
        self.isStart = False
        self.turn = 0

    def placeonBoard(self,x, y, pion):
        if (self.board[x][y] == 0) and (self.isStart):
            self.board[x][y] = pion
            self.isWin(x,y,pion)

    def getboarditem(self, x, y):
        return self.board[x][y]

    def countIdentic(self, x0, y0, xi, yi, pion):
        xincr = x0 + xi
        yincr = y0 + yi
        count = 0
        temp = pion
        while (temp == pion and xincr >= 0 and yincr >= 0 and xincr < 20 and yincr < 20 ):
            temp = self.board[xincr][yincr]
            if (temp == pion):
                count += 1
            xincr+= xi
            yincr+= yi

        return count

    def CheckWin(self, x0, y0, xi, yi, pion):
        count1 = self.countIdentic(x0, y0, xi, yi, pion)
        count2 = self.countIdentic(x0, y0, -xi, -yi, pion)

        return count1 + count2 + 1 > 4

    def checkVertical(self, x0, y0, pion):
        return self.CheckWin(x0, y0, 0, 1, pion)

    def checkHorizontal(self, x0, y0, pion):
        return self.CheckWin(x0, y0, 1, 0, pion)

    def checkDiagonal(self, x0, y0, pion):
        return self.CheckWin(x0, y0, 1, 1, pion)

    def checkDiagonalReverse(self, x0, y0, pion):
        return self.CheckWin(x0, y0, -1, -1, pion)

    def isWin(self, x, y, pion):
        if self.checkVertical(x, y, pion) or self.checkDiagonal(x, y, pion) or self.checkDiagonalReverse(x, y, pion) or self.checkHorizontal(x, y, pion):
            return True

    def isGameStarted(self):
        return self.isStart

    def startGame(self):
        self.isStart = True

    def stopGame(self):
        self.isStart = False

    def addPlayer(self,userid,pion):
        self.playerlist[userid] = pion

    def removePlayer(self, userid):
        del self.playerlist[userid]

    def getTurn(self):
        return self.turn

    def nextTurn(self):
        self.turn+=1
        if self.turn >= len(self.playerlist): #Jika sudah giliran ke player maks, mulai lagi dari 0
            self.turn = 0
