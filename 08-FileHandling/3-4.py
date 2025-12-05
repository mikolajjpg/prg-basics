###
# Calculates the total value of money spent
#
import re # module for regular expressions

# file name with shopping report
email_file = 'report.txt'

# read the content of email
with open(email_file) as file:
    content = file.read()
    email =  content

# regular expression pattern
# for amounts
pattern = ['\102', '\30' , '\15']

# extract numbers from email
# tip: findall() method returns an array
amounts = re.findall(pattern, email)

# calculate the total purchases
count = 0
for amount in amounts:
   count += int(amount)

# print result
print(count)