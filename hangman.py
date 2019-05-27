
#
# Hang Man
# Project 2
#
#


# Import OS Module For
import os
import subprocess as sp

from threading import Thread
import time

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


class Helper:
    def __init__(self):
        print('Helper class is started to use.')

    def drawLine(self, symbol):
        print(symbol * int(column))

    def writeInCenter(self, word):
        wordLength = len(word)
        halfOfColumn = int(column) / 2 - int(wordLength) / 2
        print(' ' * int(halfOfColumn), end='')
        print(word)

    def drawTitle(self, word, symbol):
        self.drawLine(symbol)
        self.writeInCenter(word)
        self.drawLine(symbol)

    def cleanConsole(self):
        try:
            if(os.name == 'posix'):
                os.system('clear')
            else:
                os.system('cls')
        except:
            print('Face to a problem when we tried to clean the screen.')
        finally:
            print('[SCREEN IS CLEARED]')


class DrawHangMan:
    def __init__(self):
        self.numberOfWrongChar = 0

    def drawNextStep(self):
        self.numberOfWrongChar += 1
        stages = ["",
                  "________        ",
                  "|               ",
                  "|        |      ",
                  "|        0      ",
                  "|       /|\     ",
                  "|       / \     ",
                  "|               "
                  ]

        print(bcolors.FAIL + 'Number of fault is ' +
              str(self.numberOfWrongChar) + bcolors.ENDC)

        print('\n'.join(stages[0:self.numberOfWrongChar]))
        # temp = ''
        # if self.step >= 0:
        #     temp = '\r O \r'
        # if self.step >= 1:
        #     temp += '- |'
        # if self.step >= 2:
        #     temp += ('- \r')
        # if self.step >= 3:
        #     temp += (' /')
        # if self.step == 4:
        #     temp += ('\ ')
        # print(temp + '\r')


class HangMan:
    def __init__(self):
        self.maxFault = 7
        self.helper = Helper()
        self.drawHangMan = DrawHangMan()
        self.choseWord()
        self.helper.cleanConsole()
        self.helper.drawTitle('Hang Man', '-')

    def choseWord(self):
        self.word = input('Please chose a word : ')
        self.maxTry = self.maxFault + len(self.word)
        self.board = '__'*len(self.word)
        # self._thread = Thread(target=self.giveATimeToMemories,
        #                  kwargs={'delay': 5000})
        # if(_thread.start()):
        self.answears = ['__']*len(self.word)
        # self.giveATimeToMemories(5)

    def giveATimeToMemories(self, delay):
        print('Memorise the word in ' + str(delay) + '/second')
        time.sleep(delay)
        print('Your Time is up...')
        time.sleep(1)
        return True

    def startTheGame(self):
        tempWord = self.word
        numberOfTry = 0
        while(self.drawHangMan.numberOfWrongChar < 7 and ''.join(self.answears) != self.word and self.maxTry > numberOfTry):
            selectedWord = input('Guess a word : ')
            if(len(selectedWord) > 1):
                print(bcolors.WARNING + 'Word is changed : ' + selectedWord +
                      ' to ' + selectedWord[0:1] + bcolors.ENDC)
                selectedWord = selectedWord[0:1]
            numberOfTry += 1
            # print('STEP====> ' + str(self.drawHangMan.step))
            # print('TEMP ====> ' + tempWord)
            # print('LEN TEMP ====> ' + str(len(tempWord)))
            position = tempWord.find(selectedWord)
            if(position == -1):
                self.drawHangMan.drawNextStep()
            else:
                tempWord = tempWord[:position] + '_' + \
                    tempWord[position+1:]
                self.answears[position] = selectedWord
                print((' ').join(self.answears))
        if ''.join(self.answears) != self.word:
            print(bcolors.FAIL + 'Unfortunately you lost the game...' +
                  bcolors.ENDC)
        else:
            print(bcolors.OKGREEN + 'You won the game with ' +
                  str(self.drawHangMan.numberOfWrongChar + 1) + ' fault' + bcolors.ENDC)


hangMan = HangMan()
hangMan.startTheGame()
