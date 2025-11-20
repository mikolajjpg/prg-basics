#The following program sums numbers input by the user until they enter 0.
#Modify the program so that it also calculates the arithmetic mean of the numbers.

###
# Sums numbers entered by user
#
total_sum = 0

while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number

print(f"The total sum of the numbers is: {total_sum}")

