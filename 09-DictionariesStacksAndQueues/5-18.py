#The file dogs.json contains data about dogs.
#Write a program that prints information about dogs younger than 5 years.

import json

with open('dogs.json', 'r', encoding="utf-8") as file:

    content = json.load(file)


    for dog in content:
        for key, value in dog.items():
            if key == "age" and value <  5:
                for key, value in dog.items():
                    print(f'{key} : {value}')
                print()
                    