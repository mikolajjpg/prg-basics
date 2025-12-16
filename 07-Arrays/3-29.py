#Funkcja create_2d_arr(x,y) tworzy i zwraca dwuwymiarową tablicę o wartościach 0.
#Utwórz program i funkcję. Następnie utwórz dwuwymiarową tablicę o wymiarach 3 na 5.
#Wypisz utworzoną tablicę.

def create_2d_arr(x,y):
    arr_2d = list([0 for i in range(x) ] for i in range(y))
    return arr_2d

if __name__ == "__main__":
    print(create_2d_arr(3,5)) 