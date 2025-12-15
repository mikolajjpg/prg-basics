#Napisz program, który dla podanej tablicy liczb rzeczywistych wypisze
#liczbę elementów większych od podanej wartości wprowadzonej z klawiatury.

arr = [67, 1, 0, 5, 3, -2, 14, 9, 22]

number = int(input('Enter any number: '))

new_arr =[x for x in arr if number<x]

elements_count = 0

for element in new_arr:
    elements_count += 1

print(elements_count)