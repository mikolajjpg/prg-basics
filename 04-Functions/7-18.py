#Zdanie to uporządkowana grupa słów oddzielonych spacjami.
#Zdefiniuj funkcję f(zdanie), która zwraca zdanie bez spacji. 
#Przykładowy wynik:

#f("zintegrowane środowisko programistyczne") zwraca
#"zintegrowaneśrodowiskoprogramistyczne"
#f("Język programowania to system notacji do pisania
#programów komputerowych") zwraca
#"Językprogramowaniatosystemnotacjidopisaniaprogramówkomputerowych"

def f(zdanie):

    wynik = zdanie.replace(" ", "")

    
    

    return wynik

    


if __name__ == "__main__":
    print(f("Język programowania to system notacji do pisania programów komputerowych"))