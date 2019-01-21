#
# Function Module
# Return value as Functions insted of variable.
#
#
#
#

# Return Year of the music track
def year():
  return 2019;
# Return artist name
def artist():
  return 'Sample Artist';
# return genre of the music track
def genre():
  return 'Sample Genra';
# boolean function
def isRealized(thisYear):
  if (year() <= thisYear):
      return True
  elif year() > thisYear:
      return False;

   

print(isRealized(2018));
print(isRealized(2020));
