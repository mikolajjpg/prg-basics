#   Write a program that generates and prints a random number between 1 and 6,
#   similar to rolling a dice. Use one of the functions from the random module to
#   generate a random integer within a given range.

#   https://www.w3schools.com/python/ref_random_randint.asp

###
#   Generates and prints a random number between 1 and 6,
#   similar to rolling a dice
#
import random

def roll_dice():
    return random.randint(1,6)


print(roll_dice())