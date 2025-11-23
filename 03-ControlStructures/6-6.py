#The parking meter calculates the parking fee based on the number of
#hours the car was parked according to the following rules:

#1-2 hours: 5 PLN
#3-6 hours: 15 PLN
#Over 6 hours: 20 PLN
#Write a program that asks for the number of hours of parking,
 #then calculates and prints the correct fee.


number_of_hours = float(input('Enter number of hours of parking: '))
fee = 0


if number_of_hours < 1:
    print(f'The fee is {fee} PLN')

elif number_of_hours >= 1 and number_of_hours <= 2:
    fee = 5
    print(f'The fee is {fee} PLN')
elif number_of_hours > 2  and number_of_hours <=6:
    fee = 15
    print(f'The fee is {fee} PLN')
elif number_of_hours > 6:
    fee = 20
    print(f'The fee is {fee} PLN')
