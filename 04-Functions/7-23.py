#Prawidłowe hasło powinno składać się z co najmniej sześciu znaków,
# a każdy znak powinien występować tylko raz. Zdefiniuj funkcję f(hasło), 
 #która zwraca wartość True, jeśli hasło jest poprawne, lub False w przeciwnym razie.
#  Przykładowy wynik:

#f("ax15") zwraca False
#f("book123") zwraca False
#f("A2water3") zwraca True
#f("qwerty") zwraca True
#f("") zwraca False

def f(hasło):

    if len(hasło) != len(set(hasło)):
        return False
    else:
        return True
    

if __name__ == "__main__":
    print( f("A2water3") )   