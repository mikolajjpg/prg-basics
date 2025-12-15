#Utwórz program, który drukuje wszystkie unikalne elementy w tablicy. 
#Przykładowy wynik:

#Array: 2 3 2 5 8 1 9 8
#Unique elements: 3 5 1 9

arr = [2, 3, 2, 5, 8, 1, 9, 8]

unikalne = [number for number in arr if arr.count(number) == 1]

print("Array:", *arr)
print("Unique elements:", *unikalne)