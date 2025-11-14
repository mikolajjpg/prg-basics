#Using built-in Python functions, write a program that calculates and prints:

#the largest number: 7,5,6,3,8,2
#the smallest number: 4,7,2,3,9,8
#length of the phrase: "computer science"
#letter read from the keyboard
#number representing the string "20303"
#binary string representing decimal number 304
#hexadecimal string representing decimal number 304
#integer representing the Unicode code of the € sign
#absolute value of -17
###
# Program for testing built-in functions
#
max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number)

min_number = min(4,7,2,3,9,8)
print('Min number of 4,7,2,3,9,8 is', min_number)

str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

letter = input('Enter sth on keyboard')
print('The letter is ', letter )

number = int(20203)
print('The number is', number  )

hexable = hex(304)
print('The respresteting string is', hexable)

absolute = abs(-17)
print('The absolute value of -17 is', absolute)

