#Then, write a program that allows you to enter and print employee data.
#Due to personal data protection, 
#you can determine whether information about the employee's salary will be printed.

#Hint: when importing a module, note that:

#the name of the module to be imported 
#is given without the file name extension (only the name itself)
#the program first searches for the module in the same folder where the program is located
###
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed
#
#import keyboard # your own defined module

# Reads employee's data from keyboard

from keyboard2 import *

first_name = input_string('Enter name: ')
last_name = input_string('Enter surname: ')
age = input_integer('Enter age: ')
salary = input_real('Enter salary: ')
is_salary_hidden = input_boolean('Hide salary? (y/n)')

# Prints employee's record
print('DATA RECORD')
print('===========')
print(f'Name: {first_name}')
print(f'Surname: {last_name}')
print(f'Age: {age}')
if is_salary_hidden == False:
    print(f'Salary: {salary}')
else:
    pass