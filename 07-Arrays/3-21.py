#Napisz program, który sprawdza, czy pierwsza tablica jest podzbiorem drugiej
#(czy wszystkie elementy pierwszej tablicy pojawiają się w drugiej tablicy).

arr1 = [1,3,2,4,3,3]
arr2 = [1,2,3,4,5,6,7,8,9,2]

if set(arr1) <= set(arr2):
    print(True)
else:
    print(False)