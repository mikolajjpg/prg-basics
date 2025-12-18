#Poniższe dane zawierają informacje o liczbie produktów dostępnych w sklepie komputerowym.
#Napisz program, który wyświetli:

#listę produktów i ich ilość
#całkowitą liczbę produktów w sklepie

products ={
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}

counter = 0
for product in products:
    counter += products[product]
    
    print(f"{product}: {products[product]}")
print(counter)

