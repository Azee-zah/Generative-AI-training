while True:
    USSD_code = "*613#"
    Dial = input("Enter your Ussd_code here: ")
    if Dial != USSD_code:
        print(f"Enter the right code {USSD_code} here: ")
    else:
        print("WELCOME BACK, You can do all transactions here!")
        break
        
    
while True:
      print("\nMenu")
      print("1. Check balance")
      print("2. Withdraw")
      print("3. Buy Airtime")
      print("4. Exit")
      break
choice = input("Enter your option here: ")
balance = 30000
if choice == "1":
     print("Your balance is: #", balance)


elif choice == "2":
     amount = int(input("Enter the amount to withdraw: "))
     if amount <= balance:
        balance -= amount
        print("Withdrawal successfull!. your new balance is #", balance)
     else:
         print("Insufficient balance")



elif choice == "3":
    airtime = int(input("Enter the amount of airtime you want to buy: "))
    if airtime <= balance:
        balance -= airtime
        print("Airtime purchase successful!. new balance is # ", balance)
    else:
        print("Insufficient balance")
else:
    print("Goodbye. Thank you for banking with Hollas bank!")