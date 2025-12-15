#Utwórz moduł MyArrays zawierający funkcje do operowania na tablicy liczb:

#Funkcja zwracająca drugi co do wielkości element tablicy
#Funkcja zwracająca różnicę między największą a najmniejszą wartością tablicy
#Funkcja zwracająca medianę liczb w tablicy.
#Nie używaj funkcji wbudowanych. Mediana to wartość środkowa w uporządkowanym ciągu liczb:

#A function that returns a two-element array containing the smallest and largest values in an array

#A function that returns array elements as a string, separated by the minus sign

#Funkcja zwracająca dwuelementową tablicę zawierającą najmniejszą i największą wartość w tablicy

#Funkcja zwracająca elementy tablicy jako ciąg znaków, oddzielone znakiem minus

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
    current_max = arr[0]
    for values in arr:
        if current_max < values:
            current_max = values

    new_arr = [number for number in arr if number != current_max]
    vice_max1 = 0
    for values2 in new_arr:
        if vice_max1 < values2:
            vice_max1 = values2

    return vice_max1

def minus_separation(arr):
    wynik2 =""
    for values in arr:
        wynik2 = wynik2 + '-' + str(values)

    return wynik2.lstrip('-')


def bublesort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j + 1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


def median(arr):
    arr2 = arr.copy()
    bublesort(arr2)
    if len(arr2) %2 !=0:
        i = len(arr2) // 2
        median_of_arr = arr2[i]
    elif len(arr2) %2 ==0:
        i = len(arr2) // 2
        counting_median = (arr2[i] + arr2[i-1]) / 2
        median_of_arr = counting_median

    return median_of_arr

def max_min(arr):
    current_max = arr[0]
    current_min = arr[0]

    for values in arr:
        if values > current_max:
            current_max = values
    for values in arr:
        if values < current_min:
            current_min = values

    wynik = [current_min, current_max]

    return wynik

if __name__=="__main__":
    print(vice_difference(numbers))
    print(vice_max(numbers))
    print(median(numbers))
    print(max_min(numbers))
    print(minus_separation(numbers))

