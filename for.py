#
# 
# 
#  The assesment is related to "Fizz Buzz" assesment
# 
# 


def isPrime(num):
  for number in range(2, num - 1):
    if(num % number == 0):
      return False
  return True

def printNumber(max):
  for number in range(max):
    if number > 2 and isPrime(number):
      print('Prime')
    if number % 3 == 0 and number % 5 == 0:
      print('FizzBuzz')
      continue
    if number % 3 == 0:
      print('Fizz')
      continue
    if number % 5 == 0:
      print('Buzz')
      continue
    print(number)


printNumber(100);
    