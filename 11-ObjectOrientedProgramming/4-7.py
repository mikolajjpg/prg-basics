class Statistics:
    def __init__(self):
        self.number_set = []
        self.maximum = 0
        self.minimum = 0
        self.average = 0
        self.mediana = 0
        

    def add_number_set(self):
        keyboard_number = int(input('Enter any number: '))
        self.number_set.append(keyboard_number)


    def display_set_of_numbers(self):
        wynik =""
        for number in self.number_set:
            wynik = wynik + " " + str(number)

        print(wynik.lstrip(' '))

    
    def greatest_number(self):
        self.maximum =max(self.number_set)

    def smallest_number(self):
        self.minimum = min(self.number_set)


    def mean(self):
        summary = 0
        for number in self.number_set:
            summary += number

        self.average = summary / len(self.number_set)

    def median(self):
        self.mediana = 0
        # 1. Najpierw sortujemy listę do nowej zmiennej
        # Używamy sorted(), żeby nie pomieszać kolejności w oryginalnej liście (do wyświetlania)
        sorted_list = sorted(self.number_set)
        n = len(sorted_list)
        
        # Zabezpieczenie na wypadek pustej listy
        if n == 0:
            return

        # 2. Sprawdzamy parzystość
        if n % 2 != 0:
            # Nieparzysta: bierzemy środkowy element
            # Bez "+1", bo indeksy są od 0
            self.mediana = sorted_list[n // 2]
        else:
            # Parzysta: bierzemy dwa środkowe
            mid1 = sorted_list[n // 2 - 1]  # Element po lewej od środka
            mid2 = sorted_list[n // 2]      # Element po prawej od środka
            # 3. Dodajemy nawias (mid1 + mid2)
            self.mediana = (mid1 + mid2) / 2
            
    def display_of_statistical_quantities(self):

        print(f"Minimum: {self.minimum}")
        print(f"Maximum: {self.maximum}")
        print(f"Mean: {self.average}")
        print(f"Median: {self.mediana}")

def main():

    my_stats = Statistics()

    my_stats.add_number_set()
    my_stats.add_number_set()
    my_stats.add_number_set()
    my_stats.add_number_set()
    my_stats.add_number_set()
    my_stats.add_number_set()
    my_stats.display_set_of_numbers()
    my_stats.greatest_number()
    my_stats.smallest_number()
    my_stats.mean()
    my_stats.median()
    my_stats.display_of_statistical_quantities()


if __name__ =="__main__":
    main()
       

        