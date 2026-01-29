balance = 1000
new_balance = []
converted_balance = []

def ATM_PIN():
    print("--- ATM PIN VERIFICATION ---")
    set_pin = int(input("Enter the PIN number for ATM PIN: "))
    attempts = 4
    for i in range(attempts):
        enter_pin = int(input("Enter your ATM PIN: "))
        if set_pin == enter_pin:
           print("ATM PIN is correct you can proceed")
           return True
        else:
            remaining_attempts = (attempts - 1) - i
            if remaining_attempts > 0:
               print(f"Incorrect. You have {remaining_attempts} attempts remaining")
            else:
                print("Try after 24 hours")
    return False

def options():
    print("\n--- MENU ---")
    res = int(input("1. Deposit\n2. Balance check\n3. Withdrawal\n4.CurrencyConvert\n5. Exit\nSelection: "))
    return res

def balance_check(current_balance):
    print(f"Current Balance: {current_balance}")

def Deposit():
    global balance
    deposit_amount = float(input("Enter your deposit amount: "))
    balance += deposit_amount
    new_balance.append(f"Deposit: +{deposit_amount}")
    print(f"Updated balance: {balance}")

def withdraw():
    global balance
    withdrawl_amount = float(input("Enter your Withdraw amount: "))
    if withdrawl_amount <= balance:
        balance -= withdrawl_amount
        new_balance.append(f"Withdrawal: -{withdrawl_amount}")
        print(f"Updated balance: {balance}")
    else:
        print("Insufficient funds")

def CurrencyConvert():
    print("\n--- Currency_type-------")
    choice = int(input("1.USD\n2.EURO\n3.AUD\n4.CAD\n5.JPY\n6.withdraw1\n7.EXIT\nSelection: "))
    return choice

def USD():
    global balance
    converted = balance / 83.0
    print(f"Your balance in USD: ${round(converted, 2)}")

def EURO():
    global balance
    converted = balance / 90.0
    print(f"Your balance in EURO: €{round(converted, 2)}")

def AUD():
    global balance
    converted = balance / 55.0
    print(f"Your balance in AUD: A${round(converted, 2)}")

def CAD():
    global balance
    converted = balance / 60.0
    print(f"Your balance in CAD: C${round(converted, 2)}")

def JPY():
    global balance
    converted = balance / 0.55
    print(f"Your balance in JPY: ¥{round(converted, 2)}")

def withdraw1():
    choice = int(input("your county currency name 1.USD\n2.EURO\n3.AUD\n4.CAD\n5.JPY\n6.EXIT: "))
    return choice

def withdraw_in_usd():
    global balance
    rate = 83.0
    converted = balance / rate
    withdrawlAmount = float(input("Enter your Withdraw amount in USD: "))
    if withdrawlAmount <= converted:
        balance -= (withdrawlAmount * rate)
        converted_balance.append(f"Withdrawal: -{withdrawlAmount} USD")
        print(f"Remaining balance: {balance}")
    else:
        print("Insufficient funds")

def withdraw_in_euro():
    global balance
    rate = 90.0
    converted = balance / rate
    withdrawlAmount = float(input("Enter your Withdraw amount in EURO: "))
    if withdrawlAmount <= converted:
        balance -= (withdrawlAmount * rate)
        converted_balance.append(f"Withdrawal: -{withdrawlAmount} EURO")
        print(f"Remaining balance: {balance}")
    else:
        print("Insufficient funds")

def withdraw_in_aud():
    global balance
    rate = 55.0
    converted = balance / rate
    withdrawlAmount = float(input("Enter your Withdraw amount in AUD: "))
    if withdrawlAmount <= converted:
        balance -= (withdrawlAmount * rate)
        converted_balance.append(f"Withdrawal: -{withdrawlAmount} AUD")
        print(f"Remaining balance: {balance}")
    else:
        print("Insufficient funds")

def withdraw_in_cad():
    global balance
    rate = 60.0
    converted = balance / rate
    withdrawlAmount = float(input("Enter your Withdraw amount in CAD: "))
    if withdrawlAmount <= converted:
        balance -= (withdrawlAmount * rate)
        converted_balance.append(f"Withdrawal: -{withdrawlAmount} CAD")
        print(f"Remaining balance: {balance}")
    else:
        print("Insufficient funds")

def withdraw_in_jpy():
    global balance
    rate = 0.55
    converted = balance / rate
    withdrawlAmount = float(input("Enter your Withdraw amount in JPY: "))
    if withdrawlAmount <= converted:
        balance -= (withdrawlAmount * rate)
        converted_balance.append(f"Withdrawal: -{withdrawlAmount} JPY")
        print(f"Remaining balance: {balance}")
    else:
        print("Insufficient funds")

if ATM_PIN():
    while True:
        user_choice = options()

        if user_choice == 1:
            Deposit()
        elif user_choice == 2:
            balance_check(balance)
        elif user_choice == 3:
            withdraw()
        elif user_choice == 4:
            users_choice = CurrencyConvert()
            if users_choice == 1:
                USD()
            elif users_choice == 2:
                EURO()
            elif users_choice == 3:
                AUD()
            elif users_choice == 4:
                CAD()
            elif users_choice == 5:
                JPY()
            elif users_choice == 6:
                users_choice = withdraw1()
                if users_choice == 1:
                    withdraw_in_usd()
                elif users_choice == 2:
                    withdraw_in_euro()
                elif users_choice == 3:
                    withdraw_in_aud()
                elif users_choice == 4:
                    withdraw_in_cad()
                elif users_choice == 5:
                    withdraw_in_jpy()
                else:
                    print("thank's for the visit have a good day")
            else:
                 print("good day sir")
        elif user_choice == 5:
            print("Thank you! Goodbye.")
            break
        else:
            print("Invalid choice.")

        cont = input("\nPerform another transaction? (Y/N): ").upper()
        if cont != "Y":
            print("Session closed.")
            break