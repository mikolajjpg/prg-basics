#Napisz program do rejestrowania głosowania.
#Wyniki głosowania są zapisywane w pliku vote.json o poniższej strukturze.
#Program pobiera imię i nazwisko osoby z klawiatury 
#i zwiększa liczbę głosów oddanych na tę osobę o 1.
#Jeśli jest to nowa osoba, jest ona dodawana do listy z liczbą głosów równą 1.
#Możesz uruchomić program wielokrotnie, aby dodać kolejne głosy do pliku json.

#{
   #person_name: number of votes,
   #person_name: number of votes,
#}

# Read the contents of the json file

import json

filename = 'voting.json'

try:
    with open(filename, 'r', encoding='utf-8') as file:
        votes = json.load(file)

except FileNotFoundError:

    votes = {}

person_name = input('Name of the person you are voting for: ')

if person_name in votes:
    votes[person_name] += 1
else:
    votes[person_name] = 1

with open(filename , 'w', encoding='utf-8') as file:

    json.dump(votes, file, indent=4)

    print(votes)