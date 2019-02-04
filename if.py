
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

