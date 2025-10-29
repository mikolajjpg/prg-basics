#In many games, the numbers one and six on dice have special meaning.
#Write a program that prints the number of dice rolled and the value True 
#if the number rolled is 1 or 6. Sample result:

#Dice rolled: 4
#Special number (1 or 6): False

import random

dice_roll = random.randint(1,6)
print(f'Dice rolled:{dice_roll}')
if dice_roll == 1 or dice_roll == 6: print("Special number: True")
else:
    print("Special number: False")