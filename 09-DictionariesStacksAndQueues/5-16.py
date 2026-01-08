#The computer.json file contains sample computer data.
#Open the json file in an editor and review its contents.
#Notice that the file contains a single dictionary of data.

#Then, write a program that prints information about a computer.

import json

# Open the JSON file in read mode
with open('computer.json', 'r', encoding='utf-8') as file:
   # Load the data from the JSON file into a variable
   data = json.load(file)

# Print the JSON data
for item,name in data.items():
   print(f"{item} : {name}")