#Zdefiniuj funkcję occur(liczba, tablica),
#która zwraca wartość True, jeśli dana liczba znajduje się w tablicy.
#Następnie utwórz program sprawdzający,
#czy liczba wpisana z klawiatury znajduje się w tablicy [15, 38, 7, 23, 14].
#Przykładowy wynik:

#Number: 23
#Array: 15 38 7 23 14
#Result: number 23 appears in the array

arr = [15, 38, 7, 23, 14]

def occur(liczba, tablica):
    for number in tablica:
        if number == liczba:

            return True
        
    return False
        

liczba = int(input('Enter any number: '))

wywolowanie_funkcji = occur(liczba,arr)

print(wywolowanie_funkcji)

    

