#The speed of vehicles on a highway in Poland must be between 40 and 140 km/h. 
#Write a program that checks whether the vehicle speed entered from the keyboard is correct. 
#Sample result:

#Enter vehicle speed: 158
#Speed is valid: False

speed = int(input('Enter vehicle speed: '))
if speed >= 40 and speed <= 140: print("Speed is valid: True")
else: print("Speed is valid: False")