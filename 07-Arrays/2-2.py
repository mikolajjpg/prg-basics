#Kółko i krzyżyk to prosta, ale wciągająca gra dla dwóch graczy. 
#Gra się na siatce dziewięciu pól ułożonych w trzech rzędach i trzech kolumnach.

#Poniższa tablica przedstawia planszę do gry w kółko i krzyżyk. 
#Napisz program, który wyświetla planszę na ekranie.


# 3x3 Tic-Tac-Toe board
tic_tac_toe_board = [
   ['X', 'O', 'X'],
   [' ', 'X', 'O'],
   ['O', ' ', 'X']
]

for row in tic_tac_toe_board:
   for item in row:
      print(item, end=" ")
   print()