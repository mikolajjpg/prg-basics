#Lista zawiera numery rejestracyjne pojazdów w Polsce.
#Samochody z Krakowa mają numery zaczynające się na litery „KR” lub „KK”.
#Napisz program, który drukuje numery rejestracyjne samochodów z Krakowa. 
#Ponumeruj wydrukowaną listę.

###
# Wyświetla numery rejestracyjne pojazdów z Krakowa
#
polish_license_plates = [
'KR5233F', 'PO6987E', 'KR16179', 'BI7192L', 'KK12255',
'WA7930T', 'SK6922I', 'KK61108', 'KR90538', 'BI8052Q',
'KK54985', 'LU4864U'
]
licznik = 1
counter = 1
for car_number in polish_license_plates:
    if car_number.startswith('KR') or car_number.startswith('KK'):
        print(f'{counter}. {car_number}')
        counter += 1