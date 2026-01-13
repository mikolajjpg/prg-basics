#An array contains numbers from 1 to 20. 
#Write a program that calculates and displays their third power. 
#Use the map() and an anonymous function.

arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

third_power = list(map(lambda n  : n*n*n,arr))
print(third_power)