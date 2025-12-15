#Napisz program, który oddzieli liczby parzyste od nieparzystych w danej tablicy liczb całkowitych.
#Najpierw wpisz wszystkie liczby parzyste, a następnie nieparzyste.

#Przykładowy wynik:
#arr = [7,9,2,4,5,6]
#...
#...
#arr = [2,4,6,7,9,5]

arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

arr_of_even = [number for number in arr1 if number %2 ==0]

arr_of_odd = [number for number in arr1 if number %2 !=0]

result1 = arr_of_even + arr_of_odd
result2 = arr_of_odd + arr_of_even


print(result1)
print(result2)






