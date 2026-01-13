#Write a program that calculates the sum of even numbers. 
#Use filter(), reduce() and anonymous functions.

#Tip. 
#First, use filtering to extract even numbers. 
#Then use reduce() to calculate the sum of those numbers.

from functools import reduce

numbers = [2,4,6,3,7,5]

numbers_even = filter(lambda x : x % 2 ==0,numbers)

result = reduce(lambda x,y : x + y, numbers_even)
print(result)