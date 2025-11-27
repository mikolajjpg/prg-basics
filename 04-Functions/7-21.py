#Zdefiniuj funkcję f(liczba1, liczba2, liczba3), 
#która zwraca różnicę między największą a najmniejszą liczbą. 
#Przykładowy wynik:

#f(7,4,9) zwraca 5
#f(2,12,8) zwraca 10

def f(liczba1, liczba2, liczba3):

    najwieksza = max(liczba1, liczba2, liczba3)
    najmniejsza = min(liczba1, liczba2, liczba3)
    
    return najwieksza - najmniejsza

if __name__ == "__main__":
    print( f(5,5,10) )

    
