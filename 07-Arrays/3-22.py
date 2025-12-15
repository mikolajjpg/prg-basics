#Zdefiniuj funkcję rand_elem(array), która zwraca losowo wybrany element tablicy.
#Używając tej funkcji, wydrukuj kilka losowo wybranych elementów tablicy.
import random
arr = [True, 1, "siema", 67, False]

def rand_elem(array):
    return array[random.randint(0,len(array)-1)]

if __name__ == "__main__":
    print(rand_elem(arr))
    print(rand_elem(arr))
    print(rand_elem(arr))
