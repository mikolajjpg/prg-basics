#Tablica zawiera listę polskich imion:

#Genowefa, Onufry, Celestyna, Alojzy, Pankracy
#Utwórz program, który wyświetla najdłuższe imię (składające się z największej liczby znaków). 
#Przykładowy wynik:

#Names: Genowefa Onufry Celestyna Alojzy Pankracy
#Longest name: Celestyna

arr = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

arr_string = ""
for name in arr:
    arr_string = arr_string + " " + name

print(f'Names: {arr_string.lstrip(" ")}')

current_max = arr[0]

for name in arr:
    if len(name) > len(current_max):
        current_max = name

print(f'Longest name: {current_max}')




