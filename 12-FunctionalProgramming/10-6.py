#Measuring stations recorded the following temperatures in degrees Celsius:

#{"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
#Write a program that creates a bar chart showing temperatures recorded in cities.
#Add a title for the chart and descriptions for the x and y axes.

#Tip: use the map() function to create two arrays of data for the chart.



import matplotlib.pyplot as plt

measurments = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

cities = list(map(lambda x: x[0],measurments.items()))
temps = list(map(lambda x : x[1], measurments.items()))


plt.bar(cities, temps)

plt.title("Temperatures recorded in cities")
plt.xlabel('City')
plt.ylabel('Temperature (*C)')

plt.show()

