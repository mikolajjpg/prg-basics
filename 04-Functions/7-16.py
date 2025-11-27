#Zdefiniuj funkcję f(n), która zwraca n-tą wartość ciągu Fibonacciego. 
#Ciąg jest zdefiniowany w następujący sposób: pierwsza wartość ciągu to 0, druga to 1. 
#Każda kolejna wartość jest sumą dwóch poprzednich. Przykładowy wynik:

#f(5) zwraca 3
#f(9) zwraca 21

def f(n):
    a, b = 0, 1
    for x in range(n-1):
        
        a, b = b, a + b

        

    return a





if __name__ == "__main__":
    print(f(5))