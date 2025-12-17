#Plik pets.txt zawiera humorystyczny tekst o zwierzętach.
#Napisz program, który wyświetla tekst i zlicza liczbę słów w tekście.

#Aby obliczyć liczbę słów w wierszu, użyj metody split(),
#która dzieli ciąg znaków na listę, gdzie każde słowo jest elementem listy.
#Następnie odczytaj długość tej listy. Użyj funkcji len().
#Na koniec zsumuj liczbę słów w każdym wierszu.

with open("pets.txt", 'r') as file:
    content = file.read()

    
splited_content = content.split()
print(content)
print(len(splited_content))