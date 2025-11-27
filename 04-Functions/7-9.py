def f(number, even):
    sum_of_digits = 0
    text_number = str(number)
    for char in text_number:
        numerical_char = int(char)
        
        is_even = (numerical_char % 2 == 0)

        if is_even == even:
            sum_of_digits = sum_of_digits + numerical_char   
        
           

        
    return sum_of_digits
    
if __name__ == "__main__":
    print( f(3124,False)   )
