def money():
    balance=1000.00
    print("You have $", balance)
    
def atm_withdrawal(balance):
    withdrawal= float(input("Enter withdrawal amount: "))
    if withdrawal < balance:
        print("withdrawal successful")
    elif withdrawal == balance:
        print("Balance will be zero")
    else :
    		print("insufficent balance")
            
atm_withdrawal(1000)
    

    
    
      