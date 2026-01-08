#Fotoradar rejestruje przejeżdżające pojazdy.
#Zapisuje ich numery rejestracyjne w pliku „pojazd.txt”.
#Napisz program, który oblicza i wyświetla liczbę zarejestrowanych samochodów
#z każdego województwa w Polsce. 
#Lista województw i odpowiadające im pierwsze litery numerów rejestracyjnych pojazdów 
#znajduje się w pliku „province.csv”.

#Wskazówka: skorzystaj ze słownika zawierającego litery odpowiadające województwom 
#oraz numery pojazdów, których pierwsze litery numeru rejestracyjnego 
#pokrywają się z literami nazwy województwa.

with open("province.csv" , 'r', encoding='utf-8') as file:
    content = file.read()

with open("vehicle.txt" , 'r', encoding="utf-8") as file2:
    content2 = file2.read()

slownik_wojewodzt = {}
province_splited = content.splitlines()

for line in province_splited:

    place = line.split(',')
    if len(place) == 2:
        litera = place[0]
        nazwa = place[1]
        slownik_wojewodzt[litera] = nazwa

counter = {}

rejestracje = content2.splitlines()

for auto in rejestracje:
    if len(auto) > 0:
        pierwsza_litera = auto[0]

        if pierwsza_litera in slownik_wojewodzt:
            wojewodztwo = slownik_wojewodzt[pierwsza_litera]

            if wojewodztwo in counter:
                counter[wojewodztwo] += 1
            else:
                counter[wojewodztwo] = 1

print(counter)