#The cities.json file contains data about selected cities in Poland.
#Open the json file in an editor and review its contents.
#Notice that the file contains an array of dictionaries.

#Then, write a program that prints information about cities.

#Note: using the encoding='utf-8' parameter when opening the file is necessary because 
#the json file also contains Polish characters in city names that must be processed correctly.
#Remember to always use this parameter when opening files that contain characters other
#than those in the Latin alphabet.

import json

# Open the JSON file in read mode
with open('cities.json', 'r', encoding='utf-8') as file:
   # Load the data from the JSON file into a variable
   data = json.load(file)

# Print the JSON data
for city in data:
   for key , value in city.items():
      print(key,':',value)
   print()