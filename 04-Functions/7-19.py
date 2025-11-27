#Zdefiniuj funkcję f(liczba), która zwraca sumę powtórzonych cyfr w liczbie. Przykładowy wynik:

#f(1027) zwraca 0
#f(230335) zwraca 9
#f(513553007) zwraca 21

def f(liczba):

    text_liczba = str(liczba)

    ile1 = text_liczba.count('1')
    ile2 = text_liczba.count('2')
    ile3 = text_liczba.count('3')
    ile4 = text_liczba.count('4')
    ile5 = text_liczba.count('5')
    ile6 = text_liczba.count('6')
    ile7 = text_liczba.count('7')
    ile8 = text_liczba.count('8')
    ile9 = text_liczba.count('9')


    wynik1 = 0
    wynik2 = 0
    wynik3 = 0
    wynik4 = 0
    wynik5 = 0
    wynik6 = 0
    wynik7 = 0
    wynik8 = 0
    wynik9 = 0

    if ile1 >= 2:
        wynik1 = wynik1 + ile1*1
    if ile2 >= 2:
        wynik2 = wynik2 + ile2*2
    if ile3 >= 2:
        wynik3 = wynik3 + ile3*3
    if ile4 >= 2:
        wynik4 = wynik4 + ile4*4
    if ile5 >= 2:
        wynik5 = wynik5 + ile5*5
    if ile6 >= 2:
        wynik6 = wynik6 + ile6*6
    if ile7 >= 2:
        wynik7 = wynik7 + ile7*7
    if ile8 >= 2:
        wynik8 = wynik8 + ile8*8
    if ile9 >= 2:
        wynik9 = wynik9 + ile9*9

    return wynik1 + wynik2 + wynik3 + wynik4 + wynik5 + wynik6 + wynik7 + wynik8 + wynik9

if __name__ == "__main__":
    print( f(513553007) )