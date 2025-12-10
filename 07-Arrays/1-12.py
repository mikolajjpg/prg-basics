#Monthly expenses and their corresponding expense categories are included in
#the arrays below. 
#Write a program that calculates which expense category was the most expensive.

categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]


most_expensive = max(expenses)

index_of_max = expenses.index(most_expensive)

print(categories[index_of_max])