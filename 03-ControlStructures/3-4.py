#A user enters two integer numbers from the keyboard. 
#Write a program that checks whether at least one of them is not negative.

###
# Checks whether at least one number entered
# from the keyboard is not negative
# 
x = int(input('Enter first number: '))
y = int(input('Enter second number: '))

if not x < 0 or  not y < 0  :
    print(f'At least one of the numbers {x} and {y} is not negative')
else:
    print(f'Both of the number {x} and {y} are negative')