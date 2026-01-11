#Obiekt zawiera listę współrzędnych punktów na płaszczyźnie w postaci dwuwymiarowej tablicy.
#Zdefiniuj klasę C, która umożliwia utworzenie obiektu.
#Podaj listę współrzędnych punktów w momencie tworzenia obiektu.
#W klasie C zdefiniuj metodę m(n), która zwraca wartość true, gdy co najmniej n punktów
#znajduje się w pierwszej ćwiartce układu współrzędnych (obie współrzędne punktów są większe od 0),
#lub false w przeciwnym przypadku. 
#Przykładowy wynik:

#C([[2,3],[1,8],[-6,4],[3,-7]])
#m(2) returns True
#m(3) returns False

class C:
    def __init__(self,point):

        self.point = point
       

    def m(self,n):
        counter = 0
        for location in self.point:

            if location[0] > 0 and location[1] > 0:
                counter += 1
        
        if counter >= n:
            return True
        else:
            return False
        
def main():

    my_array = C([[2,3],[1,8],[-6,4],[3,-7]])

    print(my_array.m(2))
    print(my_array.m(3))


if __name__ == "__main__":
    main()    
        