
    #Napisz program, który wyświetla pierwsze pięć wierszy pliku it_company.csv,
#a następnie w kolejnym wierszu wyświetla komunikat „Naciśnij klawisz Enter…” 
#i czeka na naciśnięcie klawisza Enter.
#Program powtarza wypisywanie kolejnych pięciu wierszy pliku,
#za każdym razem czekając na naciśnięcie klawisza Enter.

with open("it_company.csv", 'r') as file:

    

    counter = 0  # Twój licznik
    
    for line in file:
        print(line, end="") # Wypisujemy linię
        counter += 1        # Dodajemy 1, bo wypisaliśmy linię
        
    # Jeśli wypisaliśmy już 5 linii...
        if counter == 5:
            input("\nNaciśnij Enter...") # ...czekamy na klawisz
            counter = 0                  # ...i zerujemy licznik, żeby liczył od nowa
    
