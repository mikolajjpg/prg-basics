#Tablica zawiera liczby całkowite: 34, 7, 19, 4, 21, 8. 
#Utwórz program, który oblicza i wyświetla liczbę wartości parzystych w tablicy.
#Użyj instrukcji pętli „while”.

arr = [34, 7, 19, 4, 21, 8]
even_count = 0
for number in arr:
    if number % 2 == 0:
        even_count += 1

print(even_count)

#even_count = 0
#index = 0

#while index < len(arr):

    #if arr[index] % 2 == 0:
        #even_count += 1
    
    #index += 1

#print(even_count)