#An array contains numbers from 1 to 20. 
#Write a program that displays only numbers divisible by 2 and 3 without remainder. 
#Use the filter() and an anonymous function.


arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

divisible_by_two_and_three = list(filter(lambda n : n % 6 ==0,arr))

print(divisible_by_two_and_three)



