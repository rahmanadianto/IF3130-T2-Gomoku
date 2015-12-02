

class Board:
    def __init__(self,connect):
        self.size = 20
        #self.playerlist = [[], [], []] #default player : 3
        self.board = [["0" for x in range(20)] for x in range(20)]
        self.win = False

    def placeonBoard(self,x, y, pion):
        if (self.board[x][y] == 0):
            self.board[x][y] == pion

    def countIdentic(self, x0, y0, xi, yi, pion):
        xincr = x0 + xi
        yincr = y0 + yi

        count = 0
        temp = pion
        while (temp == pion):
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
