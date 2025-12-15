#Tablica zawiera liczby naturalne: 15, 8, 31, 47, 2, 19.
#Utwórz program, który wyświetla zawartość tablicy w odwrotnej kolejności.
#Użyj dowolnej instrukcji pętli.
#Przykładowy wynik:

#existed array: 15 8 31 47 2 19 
#reverse array: 19 2 47 31 8 15

arr = [15, 8, 31, 47, 2, 19]

reverse_arr = ""
for number in arr[::-1]:
    reverse_arr = reverse_arr +" "+ str(number)
normal_arr =""
for number in arr:
    normal_arr = normal_arr + " " + str(number)

    
print(f'existed array: {normal_arr.lstrip(' ')}')
print(f'reverse array: {reverse_arr.lstrip(' ')}')

    

    
