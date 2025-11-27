#Zdefiniuj funkcję f(x,y), która zwraca liczbę ujemnych liczb parzystych w zakresie <x,y>.
#Przykładowy wynik:

#f(-7,8) zwraca 3
#f(-1,11) zwraca 0

def f(x,y):
    negative_even_count = 0
    for i in range(x,y+1 ):

        if i % 2 != 0 and i >= 0:
            pass
        elif i % 2 == 0 and i < 0:
            negative_even_count = negative_even_count + 1

    return negative_even_count

if __name__ == "__main__":
    print( f(-1,11) )