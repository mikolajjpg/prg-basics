#A computer program analyses the price of a product in an online store.
#If the product price decreases by at least 10%, the program prints a purchase recommendation:

#Buy the product!!
#Product price reduced by 17%

#Create such program. The current and previous price of the product are included in variables.
#Sample result:

#Current product price: 140.00
#Previous product price: 200.00
#Buy the product!!
#Product price reduced by 30%
import random
start_price = float(input('Enter start price: '))
a = random.randint(1,100)
procent_off = (((a*0.01)*start_price) / start_price) * 100
new_price = start_price - (start_price*(a*0.01))

if procent_off >= 10:
    print(f'Current product price:{new_price:.2f}')
    print(f'Previous product price:{start_price:.2f}')
    print("Buy the product!")
    print(f'Product price reduced by {procent_off}%')
else:
    print(f'Current product price:{new_price:.2f}')
    print(f'Previous product price:{start_price:.2f}')