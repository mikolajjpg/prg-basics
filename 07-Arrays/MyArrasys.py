#Utwórz moduł MyArrays zawierający funkcje do operowania na tablicy liczb:

#Funkcja zwracająca drugi co do wielkości element tablicy
#Funkcja zwracająca różnicę między największą a najmniejszą wartością tablicy
#Funkcja zwracająca medianę liczb w tablicy.
#Nie używaj funkcji wbudowanych. Mediana to wartość środkowa w uporządkowanym ciągu liczb:

#A function that returns a two-element array containing the smallest and largest values in an array

#A function that returns array elements as a string, separated by the minus sign

#Then, write a program that for the sequence of numbers:

#7,3,8,5,2
#calculates and prints results. Sample result:

#Numbers: 7,3,8,5,2
##Second largest number: 7 
#Median: 5
#Smallest and largest number: 2,8
#Numbers as a string: 7-3-8-5-2
numbers = [7,3,8,5,2]
def vice_difference(arr):
    current_max = arr[0]
    for values in arr:
        if current_max < values:
            current_max = values

    current_min = arr[0]
    for values2 in arr:
        if current_min > values2:
            current_min = values2
    wynik = current_max - current_min


    return wynik

def vice_max(arr):
    current_max = 0
    for values in arr:
        if current_max < values:
            current_max = values

    new_arr = [number for number in arr if number != current_max]
    vice_max1 = 0
    for values2 in new_arr:
        if vice_max1 < values2:
            vice_max1 = values2

    return vice_max1

if __name__=="__main__":
    print(vice_difference(numbers))
    print(vice_max(numbers))

