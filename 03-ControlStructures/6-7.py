#Write a program that asks the user for their age and then
 #checks which age group they belong to:

#Child: under 13
#Teen: 13 to 19
#Adult: 20 to 64
#Senior: 65 or older


age = int(input('Enter your age: '))

if age < 13:
    print(f'{age} is Child')
elif age >= 13 and age <=19:
    print(f'{age} is Teen')
elif age >= 20 and age <= 64:
    print(f'{age} is Adult')
elif age >= 65:
    print(f'{age} is Senior')