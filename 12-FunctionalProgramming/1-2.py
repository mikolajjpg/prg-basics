# takes two numbers from keyboard
n1 = input('Enter number: ')
n2 = input('Enter number: ')

# define an anonymous function
x =int(n1)
y=int(n2)
mean = lambda x,y: (x+y)/2


# calculates arightmtic mean and print result
result = mean(n1,n2)
print(f"The arithmetic mean of {result}")