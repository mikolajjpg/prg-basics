#Napisz program, który umożliwia utworzenie listy zakupów.
#Program pobiera dane z klawiatury, aż użytkownik wprowadzi 0.
#Każda pobrana wartość jest zapisywana w pliku tekstowym „shopping_list.txt”.

#Wskazówka: Otwórz plik w trybie dopisywania, używając parametru „a” (dołącz) w funkcji open().

###
# Creates a shopping list based on product names
# entered from the keyboard.
#

# shopping list file name
shopping_list = 'shopping_list.txt'

# adds product name at the end of a shopping list
def add_product(file_name, product_name):
   with open(file_name,'a') as file:
      file.write(product_name + '\n')

# Takes next product name from the keyboard
product = ""
while product != "0":
   product = input('Enter product name (0 stops): ')
   if product == '0':
      with open(shopping_list, 'r') as file:
         content = file.read()


      print(content)   # stops entering food names ('while' breaks)
   else:
      add_product(shopping_list, product)