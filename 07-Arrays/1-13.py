#The store has 10 types of goods in stock. 
#The prices of the goods and the number of pieces of goods are given below.
#Write a program that calculates the value of all the goods available in the store.

# Prices of 10 products in the computer store (in currency units)
product_prices = [2999.99, 149.99, 499.99, 89.99, 1199.99, 349.99, 189.99, 99.99, 249.99, 999.99]

# Number of units available for each product
product_quantities = [5, 20, 10, 15, 7, 12, 25, 18, 9, 4]

product_1 = product_prices[0] * product_quantities[0]
product_2 = product_prices[1] * product_quantities[1]
product_3 = product_prices[2] * product_quantities[2]
product_4 = product_prices[3] * product_quantities[3]
product_5 = product_prices[4] * product_quantities[4]
product_6 = product_prices[5] * product_quantities[5]
product_7 = product_prices[6] * product_quantities[6]
product_8 = product_prices[7] * product_quantities[7]
product_9 = product_prices[8] * product_quantities[8]
product_10 = product_prices[9] * product_quantities[9]

total_sum = product_1 + product_2 +product_3+product_4+product_5+product_6+product_7+product_8+product_9+product_10
    


print(f'{total_sum:.2f}')