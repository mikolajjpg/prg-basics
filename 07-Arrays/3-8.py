#Tablica zawiera liczby całkowite: 2, 6, 4, 9, 7.
#Utwórz program, który graficznie wyświetla wartości tablicy, jak poniżej.
#Zdefiniuj funkcję star(n), która zwraca podaną liczbę gwiazdek jako ciąg znaków.
#Użyj zdefiniowanej funkcji w programie.

#2: **
#6: ******
#4: ****
#9: *********
#7: *******

arr = [2, 6, 4, 9, 7]


def star(n):
    return '*' * n

for number in arr:

    print(f'{number}: {star(number)}')