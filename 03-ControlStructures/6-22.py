#Write a program that prints numbers from 1 to 30. 
#If the number is divisible by 3 then the program prints the word 'THREE'.
#Next, if the number is divisible by 5 then the program prints the word 'FIVE'.
 #Finally, if the number is divisible by both 3 and 5 then the program prints the word 'BINGO'. 
# Sample result:

#     1 2 THREE 4 FIVE THREE 7 ...

for a in range(1,31):

    if a % 5 ==0 and a % 3 ==0:
        print("BINGO")

    elif a % 3 == 0:
        print("THREE")

    elif a % 5 ==0:
        print("FIVE")



    else:
        print(a)

