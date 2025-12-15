#Utwórz program, który oblicza drugą potęgę każdego elementu tablicy.
#Przykładowy wynik:

#Array: 8 2 5 1 9
#2nd power: 64 4 25 1 81

arr = [8, 2, 5, 1, 9]
number_power = ""
for number in arr:
    number_powered = number*number
    number_power = number_power + " " + str(number_powered)
numbers = ""
for number in arr:
    numbers = numbers + " " + str(number)

print(f'Array: {numbers.lstrip(" ")}')
print(f'2nd power: {number_power.lstrip(" ")}')
