#Palindrom to wyrażenie, które brzmi tak samo, gdy jest czytane od tyłu.
#Zdefiniuj funkcję f(palindrom), która zwraca wartość True, jeśli wyrażenie jest palindromem,
#lub False w przeciwnym razie. Przykładowy wynik:

#f("radar") zwraca wartość True
#f("12-11-21") zwraca wartość True
#f("book") zwraca wartość False

def f(palindrom):
    text = palindrom
    text_backwards = palindrom[::-1]
    if text == text_backwards:

        return True

    else:

        return False

if __name__ == "__main__":
    print(f("book"))
