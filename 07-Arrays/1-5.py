#Tablica zawiera wartości: 1, 2, 3, 4, 5. Napisz program, który modyfikuje wartości tablicy. 
#Wyświetla tablicę po każdej zmianie.

#Odejmij jeden od pierwszego elementu tablicy
#Zwiększ ostatni element tablicy o 4
#Pomnóż środkowy element tablicy przez 2
#Przykładowy wynik:

#Tablica: [1,2,3,4,5]
#Tablica: [0,2,3,4,5]
#Tablica: [0,2,3,4,9]
#Tablica: [0,2,6,4,9]

arr = [1,2,3,4,5]
print(f'Tablica: {arr}')

arr[0] = arr[0] - 1
print(f'Tablica: {arr}')


arr[-1] = arr[-1] + 4
print(f'Tablica: {arr}')

middle_index = (len(arr) //2 )
arr[middle_index]= arr[middle_index] *2
print(f'Tablica: {arr}')
