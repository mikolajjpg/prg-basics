import aamodule


x = int(input('Enter a number: '))
y = int(input('Enter a start of math interval(number): '))
z = int(input('Enter an end of math interval(number): '))

interval_check = aamodule.check_of_range(x,y,z)

if interval_check == True:
    result = 'yes'
else:
    result = 'no'

print(f'A number: {x}')
print(f"Number {x} in the range <{y},{z}>: {result}")
