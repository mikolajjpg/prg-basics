##The price of the product on the price tag is given before and after the discount is applied. 
# Write a program that allows you to enter the product price and discount. 
# Print the product price, discount, discounted product price, 
# and the difference between the product price before and after the discount. 
# Print all prices with two decimal places. Sample result:

Enter_price= float(input('Enter price='))
Enter_discount= float(input('Enter discount'))
Price_with_discount = Enter_price * (Enter_discount*0.01)
Discount= Enter_discount*0.01
Discounted_p_price = Enter_price * Discount
The_discouted_product = Enter_price - Discounted_p_price
Difference = Enter_price - The_discouted_product
print(f'The price is {Enter_price:.2f}.')
print(f'The discount is {Discount * 100:.0f}%. ')
print(f' The discounted product price is {The_discouted_product:.2f}. ')
print(f'The difference between the product price before and after the discount {Difference:.2f}. ')


