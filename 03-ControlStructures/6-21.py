#There are coins of 1, 2 and 5 Polish Zlotys (PLN). 
#Write a program showing any amount (natural number)
#read from the keyboard with as few coins as possible.

#   Enter the amount in PLN: 18
#   The amount of PLN 18 in coins:
#   5 PLN coins: 3
#   2 PLN coins: 1
#   1 PLN coins: 1


amount_to_pay = int(input('Enter the amount in PLN: '))
orginal_amount = amount_to_pay
amount_to_pay1 = amount_to_pay
amount_to_pay2 = amount_to_pay
amount_to_pay3 = amount_to_pay

amount_to_pay1 = amount_to_pay // 5
amount_to_pay2= (amount_to_pay % 5) // 2
amount_to_pay3 = ((amount_to_pay % 5) % 2) // 1

print(f'The amount of PLN {orginal_amount} in coins:')
print(f'5 PLN coins: {amount_to_pay1}')
print(f'2 PLN coins: {amount_to_pay2}')
print(f'1 PLN coins: {amount_to_pay3}')