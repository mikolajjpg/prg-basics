#Wygodne przetwarzanie dokumentów CSV jest możliwe dzięki modułowi CSV.
#Znajdź w internecie instrukcję obsługi tego modułu.
#Następnie napisz program, który na podstawie pliku it_company.csv wyświetli imię,
#nazwisko i adres e-mail (w podanej kolejności, bez nazwy stanowiska) osób zatrudnionych na
#stanowisku „Grafik”.
#Przykładowy wynik:

#GRAPHIC DESIGNERS
#=================
#Chris Martin,chris.martin@example.com
#Jane Taylor,jane.taylor@example.com
#...
#...

import csv

with open('it_company.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    variable = 'Graphic Designer'
    for row in reader:
        for word in row:
            if word == variable:
                print(f'{row[1]} {row[0]},{row[3]}')