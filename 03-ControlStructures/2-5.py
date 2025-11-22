#Write a program that calculates and prints the quarter of the year for a given
#month number (1..12). Then check the program's results for the months:

#12, 10, 9, 1

###
# Calculates and prints the quarter of the year for a given
# month number (1..12)
#
month = int(input('Enter month number (1..12): '))

if month >= 10:
    quarter = 4
elif month ==9 or month ==8 or month== 7:
    quarter = 3
elif month ==6 or month ==5 or month== 4:
    quarter = 2
elif month ==3 or month ==2 or month== 1:
    quarter = 1

print(f'Month {month} is in quarter {quarter}')