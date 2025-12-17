#Plik it_company.csv zawiera listę pracowników. 
#Napisz program, który wyświetla tylko pracowników na stanowisku „Inżynier oprogramowania”.
#Ponumeruj elementy na wydrukowanej liście.

#Wskazówka: Możesz sprawdzić, czy dany ciąg znaków zawiera się w innym ciągu, używając operatora „in”.

###
# Prints employees employed in a specified position.
#

# Employee List
file_name = 'it_company.txt'

# Position
job_title = 'Software Engineer'
counter = 1

with open("it_company.csv", 'r') as file:
   for line in file:
      if job_title in line:
        print(f'{counter}. {line.strip()}')
         
         
        counter += 1