#Students obtained the following test results (in points, from 0 to 100):

test_results = [
   {"name":"Peter","result":27},
   {"name":"Anna","result":63},
   {"name":"Robert","result":92},
   {"name":"Paul","result":46},
   {"name":"Barbara","result":52}]
#Write a program that displays students whose scores are between 50 and 70 points.
#Use an anonymous function and filter() function.

wynik = list(filter(lambda x : x["result"] >= 50 and x["result"] <=70,test_results ))

for student in wynik:
    print(student['name'])