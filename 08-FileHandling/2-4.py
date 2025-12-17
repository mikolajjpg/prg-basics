###
# Saves to a file a list of employees working at a specified position.
#

# file names
employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'

# Position
job_title = 'Software Engineer'

# write selected employees to a file
with open('software_engineer.txt', 'w') as file1:
   with open('it_company.csv', 'r') as file2:
      for line in file2:
         if job_title in line:
            file1.write(line)