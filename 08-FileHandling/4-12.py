#Plik books.csv zawiera listę książek.
#Napisz program, który kopiuje dane o książkach z danego gatunku do odpowiadającego mu pliku.
#Użyj funkcji, aby podzielić program na logiczne części.
#Genre --> Filename
#Fantasy --> books_fantasy.txt
#Historical --> books_historical.txt
#Romance --> books_romance.txt
#Classic --> books_classic.txt  
import csv

def filter_books(source_file, target_type, target_filename):

    with open(source_file, 'r') as f_read:
        reader = csv.reader(f_read)
        next(reader)

        matching_books = []

        for row in reader:

            if row[2] == target_type:
                matching_books.append(row)

    with open(target_filename, 'w') as f_write:
        for book in matching_books:

            line = ",".join(book)
            f_write.write(line + "\n")

filter_books('books.csv','Fantasy','books_fantasy.txt')
filter_books('books.csv', 'Historical', 'books_historical.txt')
filter_books('books.csv', 'Romance', 'books_romance.txt')
filter_books('books.csv', 'Classic', 'books_classic.txt')