#In a beverage factory, a machine fills 500ml bottles. 
#The computer checks whether the bottle has been filled correctly.
#For a 500ml bottle, the allowable tolerance is 2%. 
#In the last ten bottles checked, the filling was:

recent = [508,500,512,499,492,511,503,476,501,509]
#Write a program that calculates the percentage of incorrectly filled bottles. 
#Use the filter() along with a higher order function. 
#Sample result:

#Bottle capacity:    500ml
#Filling tolerance:  2%
#Filled bottles:     508,500,512,499,492,511,503,476,501,509
#Incorrectly filled: 30%

bottle_capacity = 500
tolerance_pct = 2
tolerance_val = bottle_capacity * (tolerance_pct / 100)

min_val = bottle_capacity - tolerance_val
max_val = bottle_capacity + tolerance_val

def error_check(min_limit,max_limit):
    return lambda x: x < min_limit or x > max_limit

incorrect_bottles = list(filter(error_check(min_val,max_val),recent))
percentage = (len(incorrect_bottles)/len(recent)) * 100



print(f'Bottle capacity:     {bottle_capacity}ml')
print(f'Filling tolerance:   {tolerance_pct}%')
print(f'Filled bottles:      {",".join(map(str, recent))}')
print(f'Incorrectly filled: {int(percentage)}%')