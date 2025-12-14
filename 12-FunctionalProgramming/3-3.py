stock = [(20,5.50),(15,8.30),(37,3.85),(4,11.60)]


result = list(map(lambda x:round(x[0]*x[1], 2) , stock ))
summary = list(map(lambda x:x sum(x), result))

print(summary)