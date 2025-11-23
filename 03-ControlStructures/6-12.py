#In one of the online stores, a 25% discount is charged for each product purchased over two.
# Write a program that calculates the amount to be paid.
#Read the number of purchased products and the product price from the keyboard. Sample result:

#Number of products purchased: 5
#Product price: 40
#Amount to pay: 170.00

number_of_products = int(input('Enter number of products: '))
product_price = float(input('Enter product price: '))
base_price = product_price*number_of_products

number_of_discounted_products = (base_price//product_price -2)
discounted_price = (number_of_discounted_products*product_price)*0.75
amount_to_pay = discounted_price + (base_price-(product_price*number_of_discounted_products))

if number_of_products > 2:
    print(f'Number of products purchased: {number_of_products}')
    print(f'Product price: {product_price}')
    print(f'Amount to pay: {amount_to_pay}')


    

