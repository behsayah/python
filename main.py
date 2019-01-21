#
# Song File
# Store song's information and print the infromation indevidualy.
#
#
#


# Artist Name
artist = 'Sample Singer';
# Song name
song = 'Sample Song';
# Album Name
album='Sample Album';
# Realease Year
year = 2019;
# The song rate
rating = 4.5;
# Duration of the song
duration = '3:14';
# Size of the file
size= '7.5 MB';
# Location of the file in cloud or local machine 
location = '/Users/your-user/musics';
# Description about the song
description = 'It is sample description for the song.';
# Singer website
web = "http://www.sample.com"

""" 
Description: It is a function to print data
Required Data: none;
Optional Data: none;
"""
def printData():
  print(artist);
  print(song);
  print(album);
  print(year);
  print(rating);
  print(duration);
  print(size);
  print(location);
  print(web);

# Call the function to print the information. 
printData();
