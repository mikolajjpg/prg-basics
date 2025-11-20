#The following program calculates the sum of even numbers from 1 to a given numbe
#N using a for loop. Modify the program. Replace the 'for' statement with a 'while' statement.

###
# Calculates the sum of even numbers from 1 to a given number N
#
N = int(input('Enter your number:'))
sum_even = 0
i=1
# Calculate the sum of even numbers
while i <= N:
    if i % 2 == 0:
        sum_even += i
    i += 1

print(f"The sum of even numbers from 1 to {N} is: {sum_even}")