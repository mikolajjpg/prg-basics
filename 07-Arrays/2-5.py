#Poniższe dane przedstawiają układ miejsc w kinie.
#Napisz program, który:

#oblicza liczbę dostępnych miejsc
#oblicza liczbę zarezerwowanych miejsc
#informuje o statusie miejsca w danym rzędzie i miejscu (dostępne lub zarezerwowane)

# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats):
   place_capacity = 0
   for place in seats:
    for chair in place:
         if chair == 'A' or chair == 'B':
            place_capacity += 1
      
   return place_capacity

def seats_available(seats):
   free_place = 0
   for place in seats:
      for chair in place:
        if chair == 'A':
            free_place += 1
   return free_place

def seats_booked(seats):
   taken_place = 0
   for place in seats:
      for chair in place:
        if chair == 'B':
         taken_place += 1
   return taken_place

def seat_status(seats, row, place):
   for seat in seats[row-1][place-1]:
    if seat == 'A':
        return "Available"
    else:
        return "Booked"
      
if __name__ == "__main__":  

    print(f'CINEMA INFORMATION TABLE')
    print(f'Total seats:{seats_total(cinema_seats)}',)
    print(f'Seats available:{seats_available(cinema_seats)}')
    print(f'Seats booked:{seats_booked(cinema_seats)}')
    print(f'Seat in row 1, place 1:{seat_status(cinema_seats,1,1)}')
    print(f'Seat in row 5, place 5:{seat_status(cinema_seats,5,5)}')
    print(f'Seat in row 3, place 5:{seat_status(cinema_seats,3,5)}')