#
#
# Draw Play board
#
#
#


# Import OS Module For
import os

# Get available console row and column
row, column = os.popen('stty size', 'r').read().split();
print('ROW : ' + row)
print('COLUMN : ' + column)


def devider():
  tempDevider = ''
  for number in range(int(column)):
    tempDevider += '#'
  print(tempDevider)

def drawPlayBoard(row, column):
  totalRow = row + (row - 1)
  totalColumn = column + (column - 1)
  for countRow in range(totalRow):
    rowString = ''
    for countColumn in range(totalColumn):
      if countRow%2 == 0:
        if countColumn%2 == 0:
          rowString += ' '
        else:
          rowString += '|'
      else:
        rowString += '-'
    print(rowString);


customRow = int(input('Enter Custom Row : '))
customColumn = int(input('Enter Custom Column : '))
# Draw Dynamic Play Board
drawPlayBoard(customRow,customColumn)
# Draw a Devider
devider()
# Covert the screen
drawPlayBoard(int(customRow/2), int(customColumn/2))