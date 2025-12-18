#Napisz program tłumaczący słowa z angielskiego na polski.
#Użytkownik wpisuje słowo w języku angielskim z klawiatury.
#Program wyświetla tłumaczenie słowa lub informację o jego niedostępności.

translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}


word = input('Enter a word in eng: ')

if word in translations:

    print(translations[word])

else:

    print("translation is unavailable")
        