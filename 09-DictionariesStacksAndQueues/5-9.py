#Fotoradar rejestruje przejeżdżające pojazdy.
#Zapisuje ich numery rejestracyjne w pliku „pojazd.txt”.
#Napisz program, który oblicza i wyświetla liczbę zarejestrowanych samochodów
#z każdego województwa w Polsce. 
#Lista województw i odpowiadające im pierwsze litery numerów rejestracyjnych pojazdów 
#znajduje się w pliku „province.csv”.

#Wskazówka: skorzystaj ze słownika zawierającego litery odpowiadające województwom 
#oraz numery pojazdów, których pierwsze litery numeru rejestracyjnego 
#pokrywają się z literami nazwy województwa.

with open("province.csv" , 'r') as file:
    content = file.read()

    print(content)