#Zdefiniuj funkcję, która przyjmuje ciąg znaków jako dane wejściowe i używa stosu do jego odwrócenia.
#Następnie napisz program, który odwróci każdy tekst wprowadzony z klawiatury.

#Wskazówka: Odłóż każdy znak ciągu na stos, a następnie zdejmij znaki, aby utworzyć odwrócony ciąg.



def reversing(text):

    stack = []

    for char in text:
        stack.append(char)

    reversed_text = ""

    while len(stack) >0:
        reversed_text += stack.pop()

    return reversed_text

if __name__ == "__main__":
    print(reversing('siabadabdadembabaxcxvjklmonopjigr'))