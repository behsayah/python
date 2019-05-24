#
# Album of singer and use Dictionary & Set
#
#
#
#


# Hold singer"s data
data = {}

def setDate():
  data["artist"] = "Sample Singer"
  data["song"] = "Sample Song"
  data["album"] = "Sample Album"
  data["year"] = 2019
  data["rating"] = 4.5
  data["duration"] = "3:14"
  data["size"] = "7.5 MB"
  data["location"] = "/Users/your-user/musics"
  data["description"] = "It is sample description for the song."
  data["web"] = "http://www.sample.com"



def printData():
  for singProperty in data:
    print(singProperty + " : " + str(data[singProperty])) 

def isValidData():
  while(True):
    key = input("Enter property : ")
    if key == '': 
      break
    value = input('Enter Value : ')
    if(key in data and str(data[key]) == value):
      print('TRUE')
    else:
      print('FALSE')

setDate()
printData()
isValidData()


