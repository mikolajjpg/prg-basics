#Zdefiniuj funkcję compare(tablica1, tablica2),
#która zwraca wartość True, jeśli obie tablice są takie same,
#lub False w przeciwnym wypadku. Dwie tablice są takie same,
#jeśli mają taką samą liczbę elementów, a wartości elementów w komórkach tablic o tym samym indeksie są równe.
#Następnie utwórz program i spróbuj porównać następujące tablice:

items1 = ["water","book","sky"]  
items2 = ["water","book","sky"]
boolean1= [True,False]   
boolean2 =[True,False,True]
numbers1 =[5,3,1]   
numbers2= [5,3,1]
number3= [3,2,1]   
numbers4= [3,2]

#Wydrukuj obie tablice i wynik porównania.
#Przykładowy wynik:

def compare(tablica1, tablica2):
    check1= ""
    check2= ""
    wynik = False
    message = ""
    for item in tablica1:
        check1 = check1 + " " + str(item)

    for item2 in tablica2:
        check2 = check2 + " " + str(item2)

    if check1 == check2:
        wynik = True
    else:
        wynik = False

    if wynik == True:
        message = message + "arrays are the same"
    if wynik == False:
        message = message + "arrays are not the same"

    return f'''Array1: {check1.lstrip()}
Array2: {check2.lstrip()}
Comparsion: {message}'''
    
        
if __name__ == "__main__":
    print( compare(number3,numbers4))

        