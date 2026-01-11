#Stadion jest podzielony na sektory, każdy oznaczony literą.
#W każdym sektorze znajduje się określona liczba kibiców. 
#Zdefiniuj klasę C, która pozwala utworzyć obiekt reprezentujący stadion z listą sektorów 
#i liczbą kibiców w sektorach. Dane, jako słownik, 
#powinny zostać przesłane do obiektu w momencie jego utworzenia. 
#Zdefiniuj w klasie metodę m1(s,n), która pozwala zmienić liczbę kibiców n w sektorze s 
#lub dodać nowy sektor s o podanej liczbie kibiców n. 
#Zdefiniuj w klasie metodę m2(s), która zwraca sumę kibiców w sektorach wymienionych w ciągu s. 
#Przykładowy wynik:

#C({"A":120,"D":150,"G":90,"K":110})
#m1("G",130)
#m2("GD") returns 280
#m2("KEJ") returns 110


class C:
    def __init__(self,sectors):
        self.sectors = sectors

    def m1(self,s,n):

        self.sectors[s] = n

    def m2(self,s):
        summary = 0
        for sector in s:
            if sector in self.sectors:   
                summary += self.sectors[sector]
    
        
        return summary

def main():

    my_stadium = C({"A":120,"D":150,"G":90,"K":110})

    my_stadium.m1("G",130)
    print(my_stadium.m2("GD"))
    print(my_stadium.m2("KEJ"))



if __name__ == "__main__":
    main()    
        
        