#Zdefiniuj funkcję f(x,y), która zwraca sumę liczb z zakresu <x,y>,
#które są całkowicie podzielne przez 2 i 3 i niepodzielne przez 4. Przykładowy wynik:

#f(1,20) zwraca 24
#f(10,30) zwraca 48


def f(x,y):
    suma= 0
    for i in range(x,y+1):
        if i % 2 == 0 and i % 3 == 0 and i % 4 != 0:
            suma = suma + i

    return suma

if __name__ == "__main__":
    print( f(10,30) ) 