#Wyrażenie zawiera operatory dodawania i odejmowania liczb jednocyfrowych.
 #Zdefiniuj funkcję f(wyrażenie), która zwraca wartość wyrażenia. 
 #Przykładowy wynik:

#f("2+3") zwraca 5
#f("3+8+1") zwraca 12
#f("2+3-4+5-0") zwraca 6


def f(wyrazenie):
   return eval(wyrazenie)

if __name__ == "__main__":
    print( f("2+3-4+5-0") ) 


