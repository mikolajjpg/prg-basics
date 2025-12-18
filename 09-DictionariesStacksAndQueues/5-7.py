#A program contains two functions:

#hotel_list(hotels) that returns a list of hotel names, separated by a comma sign
#avg_price(hotels) that returns the average room price for a given list of hotels,
# rounded to an integer value
#Write a program that calculates and displays the average price for a room
#in hotels in Krakow and Sopot and indicates in which cities hotels are cheaper.
#Sample result:

#Hotels in Krakow: …,…,…,…
#Average hotel price in Krakow: …
#Hotels in Sopot: …,…,…,…
#Average hotel price in Sopot: …
#cheaper hotels in: …

hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]

def hotel_list(hotels):
    names = [] # Pusta lista na nazwy
    for hotel in hotels:
        # Wyciągamy nazwę z POJEDYNCZEGO słownika
        names.append(hotel["name"]) 
    
    # Magiczna metoda .join() łączy elementy listy przecinkiem
    return f"{','.join(names)}"

def avg_price(hotels):
    prices = []
    for price in hotels:
        prices.append(price["price"])
    counter = 0
    for value in prices:
        counter += value

    return round(counter // len(prices))


if __name__ == "__main__":
    # 1. Obliczamy dane i zapisujemy do zmiennych
    krk_names = hotel_list(hotels_in_Krakow)
    krk_avg = avg_price(hotels_in_Krakow)
    
    sopot_names = hotel_list(hotels_in_Sopot)
    sopot_avg = avg_price(hotels_in_Sopot)

    # 2. Wyświetlamy zgodnie z wzorem w zadaniu
    print(f"Hotels in Krakow: {krk_names}")
    print(f"Average hotel price in Krakow: {krk_avg}")
    
    print(f"Hotels in Sopot: {sopot_names}")
    print(f"Average hotel price in Sopot: {sopot_avg}")

    # 3. Porównujemy liczby (teraz to zadziała, bo avg to liczby)
    if krk_avg < sopot_avg:
        print("Cheaper hotels in: Krakow")
    elif sopot_avg < krk_avg:
        print("Cheaper hotels in: Sopot")
    else:
        print("Prices are equal")



