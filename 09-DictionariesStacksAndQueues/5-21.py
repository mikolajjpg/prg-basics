#Create a dictionary that describes your favorite book or movie with at least five key-value pairs.
 #Then, create a program that writes the dictionary data to the favourite.json file.

favourities = {
    "title" : 'breaking_bad',
    "Jane" : 'Krysten Ritter',
    "Jessie" : 'Aaron Paul',
    "Year" : 2005,
    "goated" : True
}

import json

filename = "favourities.json"

with open(filename, 'w', encoding="utf-8") as file:
    json.dump(favourities, file, indent=4)

print('Data has been saved to', filename)