#Write a program, a temperature converter,
#that reads temperature in degrees Celsius from the keyboard.
#Then, the program calculates and prints the temperature in Kelvin and Fahrenheit.

###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

# user puts a value of temperature in Celsius degrees

celsius = int(input("Enter temperature in Celsius degrees:" ))

# now program calculates the value of temperature in Kelvins degrees

kelvin = celsius + 273.15

# now program calculates the value of temperature in Fahrenheit degrees

fahrenheit = (celsius * 9/5) + 32

# the program displays the converted value

print(f'The temperature in Kelvin degrees is {kelvin}, and the temperature in Fahrenheit degrees is {fahrenheit}.')


