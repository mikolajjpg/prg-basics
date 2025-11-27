def f(amount_to_pay):
    amount_to_pay1 = amount_to_pay
    amount_to_pay2 = amount_to_pay
    amount_to_pay3 = amount_to_pay
    
    ile_piatek = amount_to_pay1 // 5
    ile_dwojek = (amount_to_pay2 % 5) // 2
    ile_jednynek =((amount_to_pay3 % 5) % 2) // 1

    return ile_piatek + ile_dwojek + ile_jednynek

    
if __name__ == "__main__":
    print( f(0)   )
