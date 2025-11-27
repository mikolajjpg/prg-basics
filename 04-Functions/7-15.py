#Urządzenie w drzwiach rejestruje osoby wchodzące i wychodzące z pokoju.
 #Znak + oznacza osobę wchodzącą do pokoju, a znak -- osobę wychodzącą z pokoju.
#Zdefiniuj funkcję f(detector), która zwraca wartość True, 
#jeśli w pokoju znajdowały się co najmniej 3 osoby, lub False w przeciwnym razie. 
#Przykładowy wynik:

#f("+-+++-+---") zwraca wartość True
#f("+-+-+-+-") zwraca wartość False
#f("+-++-+--") zwraca wartość False
#f("+-++-++-+--") zwraca wartość True

def f(detector):

    liczba_osob = 0

    for char in detector:

        if char == '+':

            liczba_osob = liczba_osob + 1
            
            if liczba_osob >= 3:

                wynik = True
                
                if wynik == True:

                    return wynik

            else:
                wynik = False

        elif char == '-':

            liczba_osob = liczba_osob - 1

    
    return wynik

if __name__ == "__main__":
    print( f("+-+-+-+-") )

    