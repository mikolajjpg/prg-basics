#Plik clothing.csv zawiera listę ubrań dostępnych w magazynie.
#Napisz program, który drukuje produkty,
#których cena jest niższa niż 60 i których stan magazynowy jest mniejszy niż 40.

import csv

with open('clothing.csv', 'r') as file:
    reader = csv.reader(file)
    
    next(reader)
    

    for row in reader:
        price = float(row[5])

        stock = int(row[6])

            

        if price < 60 and stock < 40:
            print(row)
                
        