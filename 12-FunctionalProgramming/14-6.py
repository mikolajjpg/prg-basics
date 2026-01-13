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


tolerance_max = 510
tolerance_min = 490

def fill_validation(tmax,tmin,ostatnie):
    return list(filter(lambda x : x >= tmin and tmax <= 510,ostatnie))

def procent_calc(fnc):
    return list(filter(lambda x : (x/len(recent))*100,fnc))

print('Bottle capacity:     500ml')
print('Filling tolerance:   2%')
print(procent_calc(fill_validation(tolerance_max,tolerance_min,recent)))