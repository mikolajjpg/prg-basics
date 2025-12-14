#Poniższe dane przedstawiają miesięczne wydatki podzielone na kategorie i tygodnie.
#Napisz program, który oblicza i drukuje:

#całkowite wydatki dla każdej kategorii
#całkowite wydatki w każdym tygodniu
#całkowite wydatki w miesiącu

# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]
overall_expenses =0
overall_food = 0
overall_transport = 0
overall_utilities = 0
week1 = 0
week2 = 0
week3 = 0
week4 = 0
# Calculates expenses
# Use loop statements
for row in monthly_expenses:
    for item in row:
        overall_expenses = overall_expenses + item

for row_food in monthly_expenses:
    overall_food += row_food[0]

for row_transport in monthly_expenses:
    overall_transport += row_transport[1]

for row_utilities in monthly_expenses:
    overall_utilities += row_utilities[2]

for item1 in monthly_expenses[0]:
    week1 += item1

for item2 in monthly_expenses[1]:
    week2 += item2

for item3 in monthly_expenses[2]:
    week3 += item3

for item4 in monthly_expenses[3]:
    week4 += item4











        

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print(f'Food:,{overall_food}')
print(f'Transport:,{overall_transport}')
print(f'Utilities:,{overall_utilities}')
print(f'Week 1:,{week1}')
print(f'Week 2:,{week2}')
print(f'Week 3:,{week3}')
print(f'Week 4:,{week4}')
print('---------------')
print(f'TOTAL:,{overall_expenses}')