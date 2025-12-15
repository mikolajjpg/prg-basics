import MyArrasys

numbers = [7,3,8,5,2]

second_max = MyArrasys.vice_max(numbers)

median = MyArrasys.median(numbers)

min_max_val = MyArrasys.max_min(numbers)

minus_string = MyArrasys.minus_separation(numbers)

print(f"Second largest number: {second_max}")
print(f"Median: {median}")
print(f"Smallest and largest number: {min_max_val[0],min_max_val[1]}")
print(f"Numbers as a string: {minus_string}")


