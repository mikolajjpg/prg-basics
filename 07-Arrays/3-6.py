#Tablica zawiera wartości: 15, 8, 31, 47, 2, 19.
#Utwórz program, który oblicza i wyświetla tablicę oraz średnią arytmetyczną wartości tablicy.
#Użyj instrukcji pętli „while”.


arr = [15, 8, 31, 47, 2, 19]
arr_counter = 0
index = 0
while index < len(arr):
    
    arr_counter += arr[index]

    index  += 1

mean = arr_counter / len(arr)

print(arr)
print(arr_counter)
print(mean)