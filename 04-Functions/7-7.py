def f(binary_number):
    
    text = (binary_number)

    for digit_char in text:
        
        if digit_char != '1' and digit_char != '0':
            return False
        
            
            
    return True
        
        


if __name__ == "__main__":
    print( f("100101")   )
