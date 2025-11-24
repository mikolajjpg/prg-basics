#   The payment card is secured with a four-digit PIN code (0805). 
#   Write a program that checks if the PIN code entered in the payment terminal is correct. 
#   The user has up to three possibilities for entering a PIN code. 
#   In case of three unsuccessful attempts, the card is blocked. Sample result:

#   Enter the PIN code: 2398
#   Incorrect...
#   Enter the PIN code: 0912
#   Incorrect...
#   Enter the PIN code: 7860
#   Incorrect...
#   Sorry, your payment card has been blocked.



for i in range(1,4):
    pin = input('Enter the PIN code: ')
    if pin == '0805':
        print("PIN approved")
        break
    else:
        print("Incorrect...")
        if i == 3:
            print("Sorry, your payment card has been blocked.")

    