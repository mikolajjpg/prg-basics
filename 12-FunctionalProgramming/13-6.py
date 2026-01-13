#At one of the Olympic Games, the medal classification is as follows:

#Write a program that creates a bar chart showing the total number of medals won by each country.
#Add a title for the chart and descriptions for the x and y axes.

#Tip: Use the map() function to create arrays of data for your chart.

import matplotlib.pyplot as plt

medals = [{"country":"Denmark","gold":2,"silver":4,"bronze":6},
{"country":"Finland","gold":5,"silver":0,"bronze":4},
{"country":"USA","gold":12,"silver":5,"bronze":11},
{"country":"Peru","gold":0,"silver":1,"bronze":7}]

countries = list(map(lambda x : x['country'],medals))
medals_n = list(map(lambda x : x['bronze']+x['silver']+x['gold'],medals))

plt.bar(countries, medals_n)

plt.title("Medals earned by countries")
plt.xlabel("Country")
plt.ylabel("Medals")

plt.show()

