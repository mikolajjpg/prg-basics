#Tekst zawiera dowolną liczbę słów. Zdefiniuj funkcję f(nazwa), 
#która zwraca akronim (pierwsze litery wszystkich słów). 
#Przykładowy wynik:

#f("Internet of Tzeczy") zwraca "IoT"
#f("Fla Ywojej Informacji") zwraca "FYI"
#f("Python") zwraca "P"

def f(nazwa):
    
    slowa = nazwa.split()

    skrot = ""

    for x in slowa:

        skrot = skrot + x[0]

    return skrot

    

if __name__ == "__main__":
    print( f("Python") )
