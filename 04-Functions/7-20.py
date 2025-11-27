#Zdefiniuj funkcję f(n), która zwraca n-tą liczbę pierwszą.
# Liczba pierwsza to liczba naturalna większa od 1, podzielna przez 1 i tę liczbę. 
 #Przykładowy wynik:

#f(1) zwraca 2
#f(5) zwraca 11

def f(n):
    znalezione = 0
    kandydat = 2

    while True:

        jest_pierwsza = True

        for i in range(2, kandydat):
            if kandydat % i == 0:
                jest_pierwsza = False
                break

        if jest_pierwsza:
            znalezione = znalezione + 1

            if znalezione == n:
                return kandydat
            
        kandydat = kandydat + 1

if __name__ == "__main__":
    print( f(1) )

    
