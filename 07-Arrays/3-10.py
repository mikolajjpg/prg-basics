#Dwie tablice zawierają następujące liczby całkowite: [4,36,12,28,9,44,5] i [5,1,36].
#Utwórz program, który drukuje liczby z pierwszej tablicy, które nie występują w drugiej tablicy.

arr1 = [4,36,12,28,9,44,5]
arr2 = [5,1,36]

unikalne = [number for number in arr1 if number not in arr2]

print(unikalne)

