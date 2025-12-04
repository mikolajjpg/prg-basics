#Napisz program, który wypisuje nazwy popularnych gier komputerowych,
#każdą nazwę w osobnym wierszu. Użyj instrukcji while.
#Dodatkowo ponumeruj listę (wyświetlaj kolejny numer przed każdym elementem listy) i
#posortuj ją alfabetycznie (użyj jednej z wbudowanych funkcji Pythona do sortowania).

computer_games = [
"„Minecraft”", "„Fortnite”", "„Cyberpunk 2077”", "„Wiedźmin 3”",
"„League of Legends”", "„Valorant”", "„Grand Theft Auto V”",
"„Elden Ring”", "„Apex Legends”", "„Call of Duty: Warzone”"
]
computer_games.sort()
i = 0
while i < len(computer_games):
    print(f'{i+1} {computer_games[i]}')

    i += 1