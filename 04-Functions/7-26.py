#Zdefiniuj funkcję f(tekst), 
#która zwraca podany tekst,
#w którym wszystkie znaki są rozdzielone myślnikiem. Przykład:

#f("Uniwersytet") zwraca "U-n-i-v-e-r-s-i-t-y"
#f("UE") zwraca "U-E"
#f("x") zwraca "x"
#f("") zwraca ""

def f(tekst):
    tekst2 = "-".join(tekst)
    return tekst2
    

if __name__ == "__main__":
    print( f("") )

