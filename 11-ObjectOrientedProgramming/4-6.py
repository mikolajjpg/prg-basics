class Bank_Account:
    def __init__(self,bank_account_no):
        self.bank_account_no = bank_account_no
        self.balance = 0

    def display_account_balace(self):
        print(f'Bank Account No: {self.bank_account_no}')
        formatted_balance = f"{self.balance:.2f}"
        
        # 2. Potem zamień kropkę na przecinek
        final_string = formatted_balance.replace('.', ',')
        
        # 3. Wyświetl
        print(f"Balance: PLN {final_string}")

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print( "Insufficient funds on the account")

def main():

    my_account = Bank_Account('12 3456 5555 9090 1111 0000 7722')

    my_account.display_account_balace()
    my_account.deposit(25.31)
    my_account.display_account_balace()
    my_account.withdraw(31.70)
    my_account.display_account_balace()
    my_account.withdraw(14)
    my_account.display_account_balace()

    
if __name__ =="__main__":
    main()
       