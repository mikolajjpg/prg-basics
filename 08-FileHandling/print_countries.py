###
# Reads from file, line by line
#
with open('countries.txt', 'r') as file:
    for line in file:
        print(line, end="")
        
        for i, in line in enumerate(file,start=1):
            

            print(f'{i}, {line}, end=""')