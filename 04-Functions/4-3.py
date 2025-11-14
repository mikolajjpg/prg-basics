#Write a program that calculates the area of ​​a triangle based on the lengths of the triangle's sides read from the keyboard. Use the defined function.
#Then calculate the area of ​​the triangle for the following dimensions of sides a, b, and c:

#3, 4, 5 (result is 6)
#5, 12, 13 (result is 30)
#7, 24, 25 (result is 84)
###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#

import math

def triangle_area(a,b,c):
    p =  (a + b + c ) / 2
    area = math.sqrt(p *(p -a)*(p -b)*(p -c)) 
    return area
for i in range(3):
    a = float(input('Enter lenght of side'))
    b = float(input('Enter lenght of side'))
    c = float(input('Enter lenght of side'))

    print(f'The area of ​​a triangle with sides 3,4,5 is {triangle_area(a,b,c)}')
#print(f'The area of ​​a triangle with sides 5,12,13 is {triangle_area(a,b,c)}')
#print(f'The area of ​​a triangle with sides 7,24,25 is {triangle_area(a,b,c)}')