
#
# In this file we compare parameters.
#
#
#
#


#
## Return True if 2 or more parameters are equal, false is none of them are equal to any of the others.
#
def CompareVariable(a,b,c):
  if(int(a)== int(b) or int(a)==int(c) or int(b)==int(c)):
    return True;
  else:
    return False;
  
print(CompareVariable(1,2,1));




# # Variables of Click 
# click = False
# like = 0
# click = True
# # Variables of Tempreatur
# Temperatur = 14
# Thermo = 5
# # Variables of Sleeping
# Time = "Day"
# Sleepy = False
# Pajamas = 'Unknown'
# InBed = True



# def onClick():
#   try:
#     pass
#     if click == True:
#       like = like + 1
#       click = False
#     except expression as identifier:
#       pass
#       print('Except is happend');
#       print(expression)
#     else:
#       pass
#     finally:
#       pass
  

# def onTemperaturLess():
#   if Temperatur < 15:
#     Thermo += 5

# def onTemperaturOver():
#   if Temperatur >= 20:
#     Thermo -= 3

# def onSleepyAndTime():
#   if (Time == 'Night' and Sleepy == True):
#     Pajamas ='On'

# def onSleepOrTime():
#   if Time == 'Night' and Sleepy == True:
#     Pajamas = 'On'
#   elif Time == 'Morning' and InBed == True:
#     pass
#     Pajamas = 'On'
#   else:
#     Pajamas = 'Off'

# print(like)
# onClick(); 

# onTemperaturLess()
# print(Thermo)

# onTemperaturOver()
# print(Thermo)



# onSleepyAndTime()
# print(Pajamas)

# onSleepOrTime()
# print(Pajamas)