#Write a program that calculates a dog's age in dog's years. 
#For the first two years, a dog's life is equal to 10.5 human years.
#After that, each dog year is equal to 4 human years. Sample result:

#Enter the dog's age in human years: 15
#The dog's age in dog's years is 73 years.

dog_by_human_years = int(input('Enter dog is age in human years:'))

if dog_by_human_years <= 2:
   dog_by_dog_years = dog_by_human_years*10.5
   print(f'The dog is age in dog years is {dog_by_dog_years} years.')

elif dog_by_human_years > 2:
    dog_by_dog_years= dog_by_human_years - 2
    result = dog_by_dog_years*4 + 2*10.5
    
    print(f'The dog is age in dog years is {result} years.')
