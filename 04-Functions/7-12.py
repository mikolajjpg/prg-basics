#Zdefiniuj funkcję f(n), która zwraca ciąg n gwiazdek rozdzielonych ukośnikiem. 
#Przykładowy wynik:

#f(4) zwraca "*/*/*/*"
#f(1) zwraca "*"

def f(n):
    ciag = ""

    for x in range(n+1):

        if x > 0:
            
            ciag = ciag + '/' + '*'

            ciag = ciag.lstrip('/')

            

        

    return  str(ciag)

if __name__ == "__main__":
    print( f(4) )