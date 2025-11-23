#Pytania typu „tak/nie” są często używane w ankietach do oceny postaw ludzi wobec określonych
#idei lub przekonań. Napisz program, który drukuje ankietę składającą się z trzech pytań.
#Zapisz odpowiedzi jako zmienne logiczne. Następnie wyświetl wynik ankiety. 
#Przykładowy wynik:

#ANKIETA Czy interesujesz się informatyką? (t/n): t
#Czy lubisz grać w gry komputerowe? (t/n): n
#Czy masz konto na Instagramie? (t/n): t

#WYNIKI ANKIETY Zainteresowanie informatyką: Tak
#Granie w gry komputerowe: Nie
#Posiadanie konta na Instagramie: Tak

first_question = input('Are you into IT?(y/n): ')
second_question = input('Do you like to play computer games?(y/n): ')
third_question = input('Do you have an Instagram account?(y/n): ')

is_it_into = (first_question == 'y')
play_games = (second_question == 'y')
has_insta = (third_question == 'y')


if is_it_into:
    print("RESULTS Interested in IT: Yes")
else:
    print("RESULTS Interested in IT: No")

if play_games:
    print("Playing computer games: Yes")
else:
    print("Playing computer games: No")

if has_insta:
    print("Has an Instagram account: Yes")
else:
    print("Has an Instagram account: No")
