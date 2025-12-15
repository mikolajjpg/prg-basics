#Write a program that prints the tuple (10,20,30,40,50) in reverse order.
#  Sample result:
#Tuple: 10,20,30,40,50
#Reverse order: 50,40,30,20,10

my_tuple = (10,20,30,40,50)
string1 = ""
string2 = ""
for number in my_tuple:
    string1 = string1 + "," + str(number)

for number2 in my_tuple[::-1]:
    string2 = string2 + "," + str(number2)


print(f'Tuple: {string1.lstrip(",")}')
print(f'Reverse order: {string2.lstrip(",")} ')