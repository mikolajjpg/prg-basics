##Write a program that calculates how many letters are between two given letters.
#  Then, using the program, calculate how many letters are between the letters:

#A and D (2 letters)
#B and M (10 letters)
#K and K (0 letters)
###
# A program that calculates
# how many letters are between two given letters
#
first = input('Enter first letter: ')
last = input('Enter last letter: ')
first_letter_code = ord(first)
last_letter_code = ord(last)
number_of_letters = last_letter_code - first_letter_code -1 
if number_of_letters <0: number_of_letters = 0
print(f'Between {first} and {last} is {number_of_letters} letters')