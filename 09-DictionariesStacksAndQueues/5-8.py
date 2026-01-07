#Write a program to calculate the total cost of a shopping cart using a price list.

# Price list
prices = {'milk': 1.49, 'butter': 2.09, 'juice': 1.19, 'bread': 1.99}

# Shopping cart with quantities
cart = {'juice': 3, 'bread': 1, 'milk': 2}

# Calculate total cost
counter = 0
summary = 0
for item1,price in prices.items():
    for item2,amount in cart.items():
        if item1 == item2:
            counter = price * amount
            summary = summary + counter
        

print(summary)
