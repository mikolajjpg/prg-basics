#   Write a program that prints the first twenty words of the Fibonacci sequence.
#   The sequence is defined as follows: the first term is equal to 0,
#   the second is equal to 1, each subsequent term is the sum of the previous two. 
#   Sample result:

#   https://en.wikipedia.org/wiki/Fibonacci_number

#   0 1 1 2 3 5 8 13 21 34 ...

a = 0
b = 1

for i in range (0,20):
    print(a, end=' ')

    a, b = b, a + b