##Define a function that calculates and returns the sum of the digits in a number. Then write a program that reads a number from the keyboard and prints the sum of its digits.

#Steps of the algorithm to sum digits in a number:

#Take an integer input from the user. The number can be positive, negative, or zero.Handle Negative Numbers: Convert the number to its absolute value using the abs() function. 
#This step ensures the algorithm correctly processes negative numbers by ignoring the negative sign.
#Convert to String: Convert the number to a string using str(). This allows iteration over each digit in the number.
#Iterate Over Digits:
#Loop through each character (digit) in the string representation of the number.
#Convert each character back to an integer.
#Sum Digits: Add each integer value to a running total.
#Output the Result: Return the sum of the digits
###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    ...
    ...
    return ...

any_number = int(input('Enter integer number: '))
result = sum_digits(...)
print('The sum of the digits in the number ... is ...')