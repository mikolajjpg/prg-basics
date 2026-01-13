#At one of the Olympic Games, the medal classification is as follows:

medals = [
    {"country":"Denmark","gold":2,"silver":4,"bronze":6},
{"country":"Finland","gold":5,"silver":0,"bronze":4},
{"country":"USA","gold":12,"silver":5,"bronze":11},
{"country":"Peru","gold":0,"silver":1,"bronze":7}
]
#Write a program that displays the data of countries that have won at least 10 medals.
#Use anonymous and filter() functions. 
# Sample result:

#COUNTRIES WITH AT LEAST 10 MEDALS
#Denmark: 2,4,6
#USA: 12,5,11

at_least_ten = list(filter(lambda x : x['gold']+x['silver']+x['bronze'] >=10,medals))

print('COUNTRIES WITH AT LEAST 10 MEDALS')
for x in at_least_ten:
        print(f"{x['country']}: {x['gold']},{x['silver']},{x['bronze']}")
    