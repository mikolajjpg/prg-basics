class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self ,distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_recepit(self):
        print('Taxi recepit')
        print(f'Distance: {self.distance} km')
        print(f'Rate: {self.rate_per_km} per km')
        print(f'Fare: {self.fare}')
        print()


def main():
    
    ride1 = TaxiRide(1)
    ride2 = TaxiRide(2)

    ride1.calculate_fare(67)
    ride2.calculate_fare(51)

    ride1.print_recepit()
    ride2.print_recepit()
if __name__ == "__main__":
    main()
