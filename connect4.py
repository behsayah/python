#
# Connect 4 Game
#
# Simple game
# Create a Connect 4 game in Python.
#
#


# Import OS Module For
import os

# Get available console row and column
row, column = os.popen('stty size', 'r').read().split()


# Get available console row and column
row, column = os.popen('stty size', 'r').read().split()


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Connect:
    def __init__(self):
        self.getBoardWidth()
        self.getBoardHeight()
        self.buildPlayBoard()
        self.drawPlayBoard()
        self.player = 'A'
        self.winner = '-'
        self.startPlay()

    def drawLine(self, symbol):
        print(symbol * int(column))

    def writeInCenter(self, word):
        wordLength = len(word)
        halfOfColumn = int(column) / 2 - int(wordLength) / 2
        print(' ' * int(halfOfColumn), end='')
        print(word)

    def buildPlayBoard(self):
        self.board = []
        for h in range(self.row):
            tempRow = []
            for w in range(self.column):
                tempRow.append(' ')
            self.board.append(tempRow)

    def getBoardHeight(self):
        self.row = int(input('Define board height : '))

    def getBoardWidth(self):
        self.column = int(
            input(bcolors.WARNING + 'Define board width : ' + bcolors.ENDC))

    def switchPlayer(self):
        if(self.player == 'A'):
            self.player = 'B'
            return
        self.player = 'A'

    def getDropColumn(self):
        self.column = int(input('Chose Column : '))

    def drawPlayBoard(self):
        for h in range(self.row):
            rowString = ''
            print('|'.join(self.board[h]))
            print('-'*(self.row*2 - 1))

    def startPlay(self):
        isWinning = False
        self.counterNumberOfPlay = 0
        while(self.winner == '-'):

            self.drawLine('-')
            self.writeInCenter('Turn : ' + str(self.counterNumberOfPlay + 1))
            self.drawLine('-')

            column = int(input('Select column: '))
            self.counterNumberOfPlay += 1
            for r in range(self.row):
                row = self.row - r - 1
                if(self.board[row][column] == ' '):
                    self.board[row][column] = self.player
                    print('Selected spit is : ' +
                          str(row) + ':' + str(column))
                    break
            if self.horizontalWinner() or self.verticallyWinner() or self.diagonalWinnerLtr() or self.diagonalWinnerRtl():
                self.drawPlayBoard()

                self.drawLine('+')
                self.writeInCenter('Winner is ' + self.winner)
                self.drawLine('+')
                return

            self.switchPlayer()
            self.drawPlayBoard()
            # self.checkBoard()

    # def checkBoard(self):
        # playerBoard = {}
        # playerBoard["A"] = False
        # playerBoard["B"] = False
        # for r in range(2):
        #   #
        #     for w in range(self.height):
        #       #
        #         for h in range(self.width):
        #
    def diagonalWinnerLtr(self):
        if(self.winner != '-'):
            return
        tempUser = self.player*3
        for col in range(self.column - 2):
            for row in range(self.row - 2):
                temp = self.board[row][col] + self.board[row + 1][col +
                                                                  1] + self.board[row + 2][col + 2]
                # print('Matrix Row & Column : ' + str(col) + ' : ' + str(row))
                # print('LTR (temp)======> ' + temp)
                if(tempUser == temp):
                    self.winner = self.player
                    return True
        return False

    def diagonalWinnerRtl(self):
        if(self.winner != '-'):
            return
        tempUser = self.player*3
        for col in range(2, self.column):
            for row in range(self.row - 2):
                temp = self.board[row][col] + self.board[row + 1][col -
                                                                  1] + self.board[row + 2][col - 2]
                if(tempUser == temp):
                    self.winner = self.player
                    return True
        return False

    def horizontalWinner(self):
        if(self.winner != '-'):
            return
        temp = ''
        tempUser = (self.player*3)
        for h in range(self.row):
            for w in range(self.column):
                temp += self.board[h][w]
            temp += ' '

        if(tempUser in temp):
            self.winner = self.player
            return True
        return False

    def verticallyWinner(self):
        if(self.winner != '-'):
            return
        temp = ''
        tempUser = (self.player*3)
        for w in range(self.column):
            for h in range(self.row):
                temp += self.board[h][w]
            temp += ' '

        if tempUser in temp:
            self.winner = self.player
            return True
        return False


connect = Connect()
