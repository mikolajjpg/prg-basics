#Most female names in Polish end with the letter "a". 
#Write a program that prints the name entered from the keyboard,
#provided it is a female name. Sample result:

#Enter name: Anna
#Anna -- Polish female name

name = input('Enter your name: ')

last_letter = name[-1]

if last_letter.lower() == 'a':
    print(f'{name} - Polish female name')
else:
    pass
