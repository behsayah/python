myUniqueList = []

#This function just add the value, no mather what.
def add(ele):
  myUniqueList.append(ele);


def addIfUnique(ele):
  index = 0
  while index < len(myUniqueList):
    if (myUniqueList[index] == ele) :  return False
    index+=1
  myUniqueList.append(ele)
  return True


#This line just add the lement to 
add('ele-0');
add('ele-1')
print(myUniqueList);
print(len(myUniqueList));
# It should return False.
print(addIfUnique('ele-1'));
# It should add the element and return TRUE
print(addIfUnique('ele-2'));
print(myUniqueList);