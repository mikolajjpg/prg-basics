#Zdefiniuj funkcję f(n1, n2, n3), która zwraca wartość True,
#jeśli przynajmniej jedna z liczb n1, n2, n3 jest ujemna, lub False w przeciwnym wypadku.
#Przykładowy wynik:

#f(11, 6, -4) zwraca True
#f(5, 4, 14) zwraca False

def f(n1, n2, n3):
    if n1 < 0 or n2 < 0 or n3 < 0:
        validation = True
    else:
        validation = False
    
    return validation

if __name__ == "__main__":
    print( f(5,4,14) )