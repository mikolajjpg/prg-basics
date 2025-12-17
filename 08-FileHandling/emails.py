#Plik email.txt zawiera nieprzetworzoną wiadomość e-mail.
#Napisz program, który używa wyrażeń regularnych do pobierania i drukowania:

#adres e-mail nadawcy
#adres e-mail odbiorcy
#temat wiadomości e-mail
#treść wiadomości e-mail
#Dla każdego z powyższych poleceń zdefiniuj osobną funkcję (patrz poniżej)
#, która zwraca wartość odczytaną z wiadomości e-mail. Umieść te funkcje w osobnym module o nazwie emails.

#email_sender()
#email_recipient()
#email_subject()
#email_body()
import re
def email_sender(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
        pattern = r"From:.*<(\S+@\S+)>"

        result = re.search(pattern, content )

        
        if result:
            return result.group(1)
        
def email_recipient(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
        pattern = r"To:.*<(\S+@\S+)>"

        result = re.search(pattern, content)
        if result:
            return result.group(1)
        
def email_subject(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
        pattern = r"Subject:\s+(.+)"
        result = re.search(pattern, content)
        if result:
            return result.group(1)
        
def email_body(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
        pattern = r"\n\n([\s\S]+)"

        result = re.search(pattern, content)
        if result:
            return result.group(1)


    
if __name__=="__main__":
    print(email_sender("email.txt"))
    print(email_recipient("email.txt"))
    print(email_subject("email.txt"))
    print(email_body("email.txt"))









