#Using functions and constants available in the math module, write a program that calculates and prints:

#square root of 7
#natural logarithm of 5
#sine of 90 degrees
###
# To use the functions available in an external module,
# you must include that module in your program.
import math

square_root = math.sqrt(7)
print('A square root of 7 is', square_root)

natural_log = math.log(5)
print('Natural log of 5 is', natural_log)

radians = math.radians(90)
sine_of = math.sin(radians)

print('Sine of 90 degrees is', sine_of)