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

#
# This class handle all File handler
#
class FileHandler:
  def __init__(self):
    self.fileName = '';
    self.isFileExist = False;
    self.mode = '';

    print('File Handle is created')
  
  def getFileName(self):
    self.fileName = input('Give us the file name: ');
  
  def getSentence(self):
    self.sentence = input('Enter sentence : ') + '\n';

  def getLineNumber(self):
    self.line= int(input('Enter line: ')) - 1;
  
  def drawLine(self, symbol):
    print(symbol * int(column));

  def writeInCenter(self, word):
    wordLength = len(word);
    halfOfColumn = int(column) / 2 - int(wordLength) / 2;
    print(' ' * int(halfOfColumn),end = '');
    print(word);
  
  def doesTheFileExist(self):
    self.isFileExist = os.path.isfile(self.fileName + '.txt');
    return self.isFileExist;
  
  def fileWriteMode(self):
    if(self.doesTheFileExist() == False):
      self.mode = 'B';
      return;
    self.mode = ''
    print('A) Read the file')
    print('B) Delete the file and start over')
    print('C) Append the file')
    print('D) Replace a single line')
    while(self.mode != 'A' and self.mode != 'B' and self.mode != 'C' and self.mode != 'D' and self.mode != 'exit'):
      self.mode = input('Could you please chose option : ')


  def replaceLine(self):
    self.getLineNumber();
    file = open(self.fileName + '.txt', 'r')
    fileContent = file.readlines();
    if(self.line > len(fileContent)):
      print('Line number is bigger than content line')
      return;

    fileContent[self.line] = self.sentence;
    newContent = ''
    for item in fileContent:
      newContent += item;
    file = open(self.fileName + '.txt', 'w')
    file.write(newContent);


  def saveDate(self):
    _fullFileName = self.fileName + '.txt';
    if(self.mode == 'A'):
      file = open(_fullFileName);
      return print(file.read());
    if(self.mode == 'B'):
      file = open(_fullFileName, 'w');
      return file.write(self.sentence);
    if(self.mode == 'C'):
      file = open(_fullFileName, 'a');
      return file.write(self.sentence);
    if(self.mode == 'D'):
      return self.replaceLine();








fileHandler = FileHandler();

fileHandler.drawLine('-')
fileHandler.writeInCenter('Test File');
fileHandler.drawLine('-')

fileHandler.getFileName();
fileHandler.fileWriteMode();
if(fileHandler.mode != 'A'):
  fileHandler.getSentence();
fileHandler.saveDate();





