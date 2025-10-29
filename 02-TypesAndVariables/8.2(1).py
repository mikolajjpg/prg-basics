#The following program code lists the steps to
#perform to calculate the area and circumference of a circle.
#Complete the program. Then, check the program for the following data:

#r = 1 --> circumference = 6.28, area = 3.14
#r = 3 --> circumference = 18.84, area = 28.26

###
# Calculation of circle area and circumference 
#

# determine radius and PI values
# calculate area 
# calculate circumference 
# print results

import math

radius = int(input('Enter radius: '))
area = math.pi*radius**2
circumference = 2*math.pi*radius
print(f'The area is {area} and the circumference is {circumference}.')
