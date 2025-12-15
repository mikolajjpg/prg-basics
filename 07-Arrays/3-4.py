#Tablica zawiera liczby: -15, 8, -31, 47, -2, 19.
#Utwórz program, który znajduje i wyświetla liczbę maksymalną i minimalną.
#Nie używaj dostępnych funkcji.

arr = [-15, 8, -31, 47, -2, 19]

#arr1 = arr[0]
#arr2 = arr[1]
#arr3 = arr[2]
#arr4 = arr[3]
#arr5 = arr[4]
#arr6 = arr[5]

#if arr1 > arr2 and arr1 > arr3 and arr1 > arr4 and arr1 > arr5 and arr1 >arr6:
    #print(f'Max number:{arr1}')
#if arr2 > arr1 and arr2 > arr3 and arr2 > arr4 and arr2> arr5 and arr2 >arr6:
    #print(f'Max number:{arr2}')
#if arr3 > arr2 and arr3 > arr1 and arr3 > arr4 and arr3 > arr5 and arr3 >arr6:
    #print(f'Max number:{arr3}')
#if arr4 > arr2 and arr4 > arr3 and arr4 > arr1 and arr4 > arr5 and arr4 >arr6:
    #print(f'Max number:{arr4}')
#if arr5 > arr2 and arr5 > arr3 and arr5 > arr4 and arr5 > arr1 and arr5 >arr6:
    #print(f'Max number:{arr5}')
#if arr6 > arr2 and arr6 > arr3 and arr6 > arr4 and arr6 > arr5 and arr6 >arr1:
    #print(f'Max number:{arr6}')

#if arr1 < arr2 and arr1 < arr3 and arr1 < arr4 and arr1 < arr5 and arr1 < arr6:
    #print(f'Min number: {arr1}')
#if arr2 < arr1 and arr2 < arr3 and arr2 < arr4 and arr2 < arr5 and arr2 < arr6:
    #print(f'Min number: {arr2}')
#if arr3 < arr2 and arr3 < arr1 and arr3 < arr4 and arr3 < arr5 and arr3 < arr6:
    #print(f'Min number: {arr3}')
#if arr4 < arr2 and arr4 < arr3 and arr4 < arr1 and arr4 < arr5 and arr4 < arr6:
    #print(f'Min number: {arr4}')
#if arr5 < arr2 and arr5 < arr3 and arr5 < arr4 and arr5 < arr1 and arr5 < arr6:
    #print(f'Min number: {arr5}')
#if arr6 < arr2 and arr6 < arr3 and arr6 < arr4 and arr6 < arr5 and arr6 < arr1:
    #print(f'Min number: {arr6}')

current_max = arr[0]
current_min = arr[0]

for number in arr:

    if number > current_max:
        current_max = number

    if number < current_min:
        current_min = number

print(f'Max number: {current_max}')
print(f'Min number: {current_min}')