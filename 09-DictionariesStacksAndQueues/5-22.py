#Write a program that takes data from the keyboard about a purchased product:

#name
#price (real number with two decimal places)
#paid (yes/no)
#The program then saves the product data in the product.json file.
#  Pay attention to the correct data types describing the product (string, float, bool).

import json

product = {}

# read product data from keyboard
name_of_product = input('Enter name of product: ')
price = round(float(input('Enter price of the product: ')),2)
is_paid = input('Enter status of paid(y/n): ') == 'y'

product["name"] = name_of_product
product["price"] = price
product["paid"] = is_paid


# save product data to json file

filename = 'product.json'

with open(filename, 'w', encoding='utf-8') as file:
    json.dump(product, file, indent=4)