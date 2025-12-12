###
# Calculates arithmetic mean of two integer numbers
#
def mean(x,y):
   x = int(x)
   y = int(y)
   arithemtic_mean = (x+y) / 2
   return arithemtic_mean

# takes two numbers from keyboard
n1 = input('Enter first number: ')
n2 = input('Enter second number: ')

# calculates arightmtic mean and print result
result = mean(n1,n2)
print(f'The arithmetic mean of the numbers {n1} and {n2} is {result}')