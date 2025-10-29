#Write a program, a unit converter, that prints your height both in cm and in feet and inches.
#Use ue the division operator without remainder and the operator calculating the remainder
#of the division.

###
# A program that prints your height both in cm and in feet and inches.
#
cm=int(input('Enter your height: '))

# calculate the number of feet
feet = cm //30.48



# calculate the number of inches
remainder_of_feet = cm% 30.48 
inches = remainder_of_feet/2.54


print(f'I am {cm}cm tall, i.e. {feet:.2f} feet and {inches:.2f} inches.')