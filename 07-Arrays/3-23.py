#Zmienna zawiera tekst:

#Jedno jabłko dziennie trzyma lekarza z daleka

#Utwórz moduł MyText zawierający:

#Funkcję zwracającą liczbę słów w tekście
#Funkcję zwracającą uporządkowaną tablicę słów, od najdłuższego do najkrótszego
#Funkcję zwracającą alfabetycznie uporządkowaną tablicę słów
#Następnie napisz program, wywołaj funkcje i wyświetl wyniki.
#Przykładowy wynik:
#Text: An apple a day keeps the doctor away
#Number of words: 8
#Words from the longest: doctor,apple,…
#Words ordered alphabetically: a,An,apple,away,…

import MyText

sentence = "An apple a day keeps the doctor away"

word_count = MyText.couting_words(sentence)
sorting_by_len = MyText.sorting_by_len(sentence)
sorting_by_abc = MyText.sorting_by_abc(sentence)

print(f'Text: {sentence}')
print(f'Number of words: {word_count}')
print(f'Word from the longest: {",".join(sorting_by_len)}')
print(f'Words ordered alphabetically: {",".join(sorting_by_abc)}')
