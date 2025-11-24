#   A natural number greater than 1 is called a prime if it has
#   exactly 2 natural factors with the values 1 and this number. 
#   Write a program that finds N leading prime numbers.
#   Read the value of N from the keyboard. Using loop statements check 
#   that the number N is divisible only by 1 and by N.

#   Prime numbers: 2 3 5 7 11 ...

# Liczbę naturalną większą od 1 nazywamy liczbą pierwszą, jeśli ma
# dokładnie 2 czynniki naturalne o wartościach 1 i tej liczby.
# Napisz program, który znajduje N wiodących liczb pierwszych.
# Odczytaj wartość N z klawiatury. Używając instrukcji pętli, sprawdź,
# czy liczba N jest podzielna tylko przez 1 i przez N.

# Liczby pierwsze: 2 3 5 7 11 ...


amount_of_primenumber_tofind = int(input('Enter amount of prime number to find: '))
number_found = 0
number = 2

while number_found < amount_of_primenumber_tofind:

    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(number, end=" ")
        number_found = number_found + 1
    
    number = number + 1