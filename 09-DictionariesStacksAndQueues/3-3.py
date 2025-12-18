#Zdefiniuj funkcję, która zwraca wartość true,
#jeśli nawiasy kwadratowe (), {}, [] są poprawnie użyte w podanym wyrażeniu.
#W przeciwnym razie funkcja zwraca wartość false. 
#Następnie napisz program, który sprawdza poprawność poniższych wyrażeń.

#Użyj stosu. Przeczytaj kolejne znaki wyrażenia. Pomiń wszystkie oprócz nawiasów.
#Jeśli jest to nawias otwierający, umieść go na stosie. Jeśli jest to nawias zamykający,
#pobierz element ze stosu i sprawdź, czy jest to pasujący nawias otwierający.

import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_validation(expression):
    stack = queue.LifoQueue()

    for char in expression:

        if char == "(" or char == "{" or char == "[":

            stack.put(char)

        elif char == ")" or char == "}" or char == "]":

            if stack.empty():
                return False
            top_element = stack.get()

            if char == ")" and top_element != "(":
                return False
            if char == "]" and top_element != "[":
                return False
            if char == "}" and top_element != "{":
                return False
            
    return stack.empty()

    
# --- TESTOWANIE ---
expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # powinno być True
expression2 = "[(2+3]/4)"                 # powinno być False
expression3 = "(2-3*4+(5/6)"              # powinno być False

if brackets_validation(expression1):
    print("Expression 1: OK")
else:
    print("Expression 1: Błąd")

if brackets_validation(expression2):
    print("Expression 2: OK")
else:
    print("Expression 2: Błąd")

if brackets_validation(expression3):
    print("Expression 3: OK")
else:
    print("Expression 3: Błąd")
    
    