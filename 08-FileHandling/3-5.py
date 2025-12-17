#Wiele aplikacji wymaga utworzenia konta z nazwą użytkownika i hasłem, aby móc z nich korzystać.
#Często aplikacje określają wymagania dotyczące nazwy użytkownika i hasła.
#Napisz program, który sprawdza, czy nazwa użytkownika i hasło wprowadzone z klawiatury
#spełniają poniższe wymagania.
#Użyj wyrażeń regularnych.

#Nazwa użytkownika ma co najmniej 6 znaków
#Nazwa użytkownika zawiera tylko małe litery
#Hasło ma co najmniej 8 znaków
#Hasło zawiera tylko litery (małe i wielkie), cyfry i znak podkreślenia

###
# Checks the correctness of username and password
#
import re

# read username and password from keyboard
username = input('Enter your username: ')
password = input('Enter your password: ')

# pattern (criteria) for username and password
username_pattern = '^[a-z]{6,}$'
password_pattern = '^[a-zA-Z0-9_]{8,}$'

# check if username and password are ok
username_match = re.match(username_pattern,username)
password_match = re.match(password_pattern, password)

# print results
if username_match and password_match :
   print(f'Username: {username} and Password: {password} is OK.')
else:
   print("Invalid username or password.")