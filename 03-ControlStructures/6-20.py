#Napisz program konwertujący liczbę dziesiętną na liczbę binarną. 
#Aby przekonwertować liczbę dziesiętną na binarną, wykonaj następujące kroki:

#Odczytaj liczbę dziesiętną z klawiatury.
#Podziel liczbę przez 2 i zanotuj resztę.
#Podziel otrzymany iloraz przez 2 i zanotuj resztę.
#Powtarzaj ten sam proces, aż iloraz będzie równy 0.
#Zapisz wartości wszystkich reszt, zaczynając od dołu do góry. To będzie wymagana liczba binarna.
#Przykładowy wynik:

#Wprowadź liczbę dziesiętną: 12
#12(10) = 1100(2)

liczba_dziesietna = int(input("Wporwadz liczbe dziesietna: "))
liczba_poczatkowa = liczba_dziesietna

liczba_binarna = []

while liczba_dziesietna > 0:
    reszta = liczba_dziesietna % 2
    liczba_binarna.append(reszta)
    liczba_dziesietna = liczba_dziesietna //2

liczba_binarna.reverse()

print(f'{liczba_poczatkowa}(10) = ', *liczba_binarna, '(2)', sep="")

