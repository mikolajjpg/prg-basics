#Produkty są oznaczone specjalnym kodem składającym się z 3 cyfr i czwartej cyfry kontrolnej.
#Czwarta cyfra jest określana poprzez obliczenie reszty z dzielenia sumy pierwszych trzech cyfr
 #przez 7. Zdefiniuj funkcję f(product_code),
 # która zwraca wartość True, jeśli kod produktu jest poprawny, 
 # lub False w przeciwnym przypadku. 
 # Przykładowy wynik:

#f("1082") zwraca wartość True
#f("2035") zwraca wartość True
#f("1114") zwraca wartość False
#f("7071") zwraca wartość False

def f(product_code):

    product_code3 = product_code[0:3]
    
    first_number_s = product_code3[0]
    second_number_s = product_code3[1]
    third_number_s = product_code3[2]

    first_number_n = int(first_number_s)
    second_number_n = int(second_number_s)
    third_number_n = int(third_number_s)

    sum_of_three_n = first_number_n + second_number_n + third_number_n

    if sum_of_three_n % 7 == int(product_code[3]):
        return True
    else:
        return False

if __name__ == "__main__":
    print( f("7071") )   







