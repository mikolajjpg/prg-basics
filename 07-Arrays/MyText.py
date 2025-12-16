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


def couting_words(text):
    lista = text.split()
    return len(lista)

def sorting_by_len(text):

    lista = text.split()

    lista.sort(key=len, reverse = True)

    return lista

def sorting_by_abc(text):

    lista = text.split()
    lista.sort(key=str.lower)

    return lista


