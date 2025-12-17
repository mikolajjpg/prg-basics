#Napisz program, który oblicza, drukuje i zapisuje do pliku tekstowego liczby całkowite
#od 1 do 100 oraz ich drugą i trzecią potęgę.
#Przykładowy wynik:

#1,1,1
#2,4,8
#3,9,27
#...
#...

with open('numberspowers.txt', 'w') as file:
    

    for x in range(1,101):
        second_power = x*x
        third_power = x*x*x
        file.write(f'{str(x)},')
        file.write(f'{str(second_power)},')
        file.write(f"{str(third_power)}\n")

        print(f"{x},{second_power},{third_power}")

