#Utwórz program sortujący elementy tablicy zawierającej liczby całkowite.
#Zastosuj algorytm sortowania bąbelkowego.
#Zdefiniuj funkcję bubblesort(array), która zwraca posortowaną tablicę.
#Spróbuj posortować i wyświetlić dowolne trzy tablice.

def bubblesort(array):
    n = len(array)

    for i in range(n):

        for j in range(0, n-i-1):

            if array[j] > array[j + 1]:

                array[j], array[j + 1] = array[j + 1], array[j]

    return array


arr1 = [64, 34, 25, 12, 22, 11, 90]
arr2 = [5, 1, 4, 2, 8]
arr3 = [10, 9, 8, 7, 6, 5]

print(f"Wynik 1: {bubblesort(arr1)}")
print(f"Wynik 2: {bubblesort(arr2)}")
print(f"Wynik 3: {bubblesort(arr3)}")