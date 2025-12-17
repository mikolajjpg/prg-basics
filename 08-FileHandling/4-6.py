#Napisz program obliczający liczbę wierszy, znaków i słów dla dowolnego pliku tekstowego.
#Użytkownik wprowadza nazwę pliku z klawiatury.
#Użyj bloku try-except, aby uniknąć przerwania działania programu,
 #gdy użytkownik wprowadzi nazwę pliku, która nie istnieje.
 #Wypisz wynik obliczeń.
 #Aby sprawdzić, czy program działa poprawnie, znajdź 3 pliki tekstowe w internecie i przetestuj je.
 #Przykładowy wynik:
import re
file_name = input('Enter file name: ')
try:
    with open(file_name, 'r') as file:
        content = file.read()
        line_list = content.splitlines()
        number_of_lines = len(line_list)

        digit_counter = len(content)
   
        
        pattern = re.findall(r'[a-zA-Z]+', content)
        slowa_counter = len(pattern)

        print(f'Liczba wierszy: {number_of_lines}')
        print(f'Liczba znaków: {digit_counter}')
        print(f'Liczba slow: {slowa_counter}')
except FileNotFoundError:
    print("Nie znaleziono pliku")
    