#   Write a program that prints 20 integer random numbers in the range of 5 to 10.
#   Napisz program, który drukuje 20 losowych liczb całkowitych z zakresu od 5 do 10.

import random

for i in range(1,21):
    x = random.randint(5,10)
    print(x)