#Napisz program, który oblicza liczbę samogłosek w tekście wprowadzonym z klawiatury.
#Użyj wyrażeń regularnych.
import re
text = input('Enter any text: ')

pattern = r'[aeiouyąęóAEIOUYĄĘÓ]'

result = re.findall(pattern, text)

print(f'Samogłoski: {result}')
print(f'Liczba samogłosek: {len(result)}')