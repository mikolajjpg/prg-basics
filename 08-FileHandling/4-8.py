#Plik files.txt zawiera listę nazw plików.
#Napisz program, który wyświetla tylko te nazwy plików,
#których rozszerzenia składają się z dokładnie czterech znaków (np. .html).
import re
with open("files.txt", 'r') as file:
    content = file.read()

    pattern = r'\w+\.\w{4}\b'

    result = re.findall(pattern, content)

    for name in result:
        print(name)
