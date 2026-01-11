#Obiekt reprezentujący pracownika zawiera następujące dane:
#imię, nazwisko, wiek i staż pracy (liczbę przepracowanych lat).
#Zdefiniuj klasę C, która umożliwia utworzenie obiektu. 
#Podaj dane pracownika w momencie tworzenia obiektu, w podanej kolejności. 
#Zdefiniuj tekstową reprezentację obiektu w tej klasie, 
#która zawiera ciąg składający się z nazwiska, pierwszej litery imienia i stażu pracy.
#Jeśli pracownik jest dorosły (ukończył 18 lat), użyj wielkich liter, w przeciwnym razie małych.
#Przykładowy wynik:

#C("Anna","May",17,7) returns "maya7"
#C("George","Brown",21,4) returns "BROWNG4"


class C:
    def __init__(self,name,surname,age,expirience):
        self.name = name
        self.surname = surname
        self.age = age
        self.expirience = expirience

    def __str__(self):
        string = ""
    
        string =  string + self.surname + self.name[0] + str(self.expirience)

        if self.age >= 18:
            return string.upper()
        else:
            return string.lower()
        


def main():

    my_worker1 = C("Anna","May",17,7)
    my_worker2 = C("George","Brown",21,4)

    print(my_worker1)
    print(my_worker2)


if __name__ == "__main__":
    main()           



    
