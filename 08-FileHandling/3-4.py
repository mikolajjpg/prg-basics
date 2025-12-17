#Plik report.txt zawiera e-mail z raportem zakupowym. 
#Napisz program, który oblicza całkowitą wartość wydanych pieniędzy.

#Wskazówka: Aby otworzyć i odczytać plik tekstowy zawierający znaki specjalne (takie jak znak euro €), 
#należy upewnić się, że plik jest odczytywany z użyciem prawidłowego kodowania znaków. 
#Najpopularniejszym kodowaniem w takich przypadkach jest UTF-8, który obsługuje szeroki zakres znaków,
# w tym symbole specjalne. Oto przykład użycia funkcji open():
#open("example.txt", "r", encoding="utf-8")

###
# Calculates the total value of money spent
#
import re # module for regular expressions

# file name with shopping report
email_file = 'report.txt'

# read the content of email
with open(email_file, 'r', encoding="utf-8") as file:
   content = file.read()

# regular expression pattern
# for amounts
pattern = '€(\d+)'

# extract numbers from email
# tip: findall() method returns an array
amounts = re.findall(pattern, content)

# calculate the total purchases
counter = 0
for amount in amounts:
   counter += int(amount)

# print result
print(counter)