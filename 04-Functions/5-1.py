def fib2(n):
    a, b = 0, 1

    for i in range(n - 1):
        a, b=b, a + b

    return a
if __name__ == "__main__":
    print( fib2(5)   )
    print( fib2(9) )