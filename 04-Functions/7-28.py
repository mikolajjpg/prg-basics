#Sekwencja cyfr zawiera liczbę oczek wyrzuconych kostką.
 #Zdefiniuj funkcję f(kostka), która zwraca liczbę określającą
  #liczbę kostek rzuconych najwięcej razy z rzędu. 
  #Przykładowy wynik:

#f("5233165554211") zwraca 5
#f("2133") zwraca 3

def f(kostka):

    max_seria = 1
    winner = kostka[0]

    for i in range(1, len(kostka)):

        if kostka[i] == kostka[i-1]:
            aktualna_seria = aktualna_seria +1
        else:
            aktualna_seria = 1

        if aktualna_seria > max_seria:
            max_seria = aktualna_seria

            winner = kostka[i]
    
    return int(winner)

if __name__ == "__main__":
    print( f("5233165554211") )