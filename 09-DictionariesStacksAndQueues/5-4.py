#A dictionary contains course names along with the number of hours.
# Write a program that calculates and prints the total number of hours. 
# Sample results:

#the total number of hours in the winter semester is …
winter_semester = {
   "math":60,
   "programming":30,
   "history":15
}

counter = 0
for name in winter_semester:
    counter += winter_semester[name]

print(f'the total number of hours in the winter semester is {counter}')