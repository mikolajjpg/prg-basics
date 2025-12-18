#Poniższe dane zawierają cennik artykułów ze sklepu odzieżowego wraz z ich cenami.
#Z powodu sezonowej wyprzedaży sklep obniża cenę każdego artykułu o 10%.
#Napisz program, który:

#wyświetla listę produktów i ich ceny przed rabatem
#wyświetla całkowitą wartość produktów przed rabatem
#modyfikuje cennik zgodnie z rabatem (zaokrąglając ceny do dwóch miejsc po przecinku)
#wyświetla listę produktów i ich ceny po 10% rabacie
#wyświetla całkowitą wartość produktów po rabacie

price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}
counter_norabat = 0
for item in price_list:
    print(f"{item}: {price_list[item]}")

    counter_norabat += price_list[item]


print(f'Suma przed: {counter_norabat:.2f}')


for item in price_list:
    
    old_price = price_list[item]
    new_price = old_price * 0.9

    new_price = round(new_price, 2)

    price_list[item] = new_price

counter_rabat = 0

for item, price in price_list.items():
    print(f"{item}: {price}")
    counter_rabat += price

print(f'Suma po: {counter_norabat:.2f}')



