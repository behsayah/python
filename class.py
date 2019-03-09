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
class Vehicle:
  def __init__(self):
    self.model = ''
    self.make = ''
    self.year = ''
    self.weight = ''
    self.NeedsMaintenance = False;
    self.TripsSinceMaintenance = 0;
  def setModel(self):
    self.model = input('Enter the model: ')
  def setMake(self):
    self.make = input('Enter the make: ')
  def setYear(self):
    self.year = input('Enter the year: ')
  def setWeight(self):
    self.weight = input('Enter the weight: ')
  def drawLine(self, symbol):
    print(symbol * int(column));
  def writeInCenter(self, word):
    wordLength = len(word);
    halfOfColumn = int(column) / 2 - int(wordLength) / 2;
    print(' ' * int(halfOfColumn),end = '');
    print(word);
  def setAll(self):
    self.setModel();
    self.setMake();
    self.setYear();
    self.setWeight();



class Cars(Vehicle):
  def __init__(self,):
    Vehicle.__init__(self);
    self.isDriving = False;
    self.NeedsMaintenance = False;
  def Drive(self):
    self.isDriving = True;
  def Stop(self):
    if(self.isDriving == True):
      self.TripsSinceMaintenance += 1;
    if(self.TripsSinceMaintenance > 99):
      self.NeedsMaintenance = True;
    self.isDriving = False;
  def Repair(self):
    self.TripsSinceMaintenance = 0;
    self.NeedsMaintenance = False;
  def printAll(self):
    print('The model:', self.model);
    print('The make:', self.make);
    print('The year:', self.year);
    print('The weight:', self.weight);
    print('Driving Status:', self.isDriving);
    print('Does need maintenance:', self.NeedsMaintenance);
    print('Number of trips:', self.TripsSinceMaintenance);

firstCar = Cars();

firstCar.drawLine('+');
firstCar.writeInCenter('Enter Car Data');
firstCar.drawLine('+');

firstCar.setAll();


firstCar.Drive();
firstCar.Stop();

firstCar.drawLine('-');
firstCar.writeInCenter('Cars Detail')
firstCar.drawLine('-');

firstCar.printAll();