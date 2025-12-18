#Napisz program, który konwertuje dowolną liczbę naturalną na liczbę binarną.
#Użyj stosu. Aby przekonwertować liczbę, podziel ją przez 2,
#za każdym razem odkładając resztę z dzielenia na stos.
#Powtarzaj dzielenie, aż dzielona liczba będzie równa zero. 
#Następnie wyciągnij i wyświetl wszystkie wartości ze stosu.
#Przykładowy wynik dla liczby 18:

#Division	Remainder
#18 / 2 = 9	0
#9 / 2 = 4	1
#4 / 2 = 2	0
#2 / 2 = 1	0
#1 / 2 = 0	1
#SAMPLE result:
#Natural number: 18
#Binary number: 10010 

import queue

def decimal_to_binaery(number):
    stack = queue.LifoQueue()

    while number > 0:
        remainder = number % 2
        stack.put(remainder)
        number = number // 2

    print("Wynik binanry: ", end="")

    while not stack.empty():
        print(stack.get(), end="")

decimal_to_binaery(18)


