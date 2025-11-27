#Zdefiniuj funkcję f(n), która zwraca liczby od 1 do n jako ciąg znaków. 
#Przykładowy wynik:

#f(11) zwraca „1234567891011”
#f(4) zwraca „1234”

def f(n):
    lista = ""
    for x in range(1,n+1):
        lista = lista + str(x)
        


    return lista
        

    


       
        





if __name__ == "__main__":
    print( f(4) )