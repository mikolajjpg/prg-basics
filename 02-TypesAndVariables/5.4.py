##23% VAT was paid from an amount. Write a program that reads an amount from the keyboard. 
# Then, it calculates and prints both the amount and its VAT. 
# Apply formatting with two decimal places. 

Amount  = float(input('Amount='))
VAT_of_amount = (Amount*0.23)
print(f'The Amount is {Amount:.2f}.')
print(f'The VAT of the amount is {VAT_of_amount: .2f}.')