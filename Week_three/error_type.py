balance = 5000  # starting balance

print("Welcome to the ATM")
amount = input("Enter amount to withdraw: ")

try:
    amount = float(amount)  # convert input to number
    
    if amount > balance:
        raise ValueError("Insufficient funds.")
    
    balance -= amount
    print("Withdrawal successful. New balance: ₦", balance)

except :
    print("Error:")

# except Exception as e:
#     print("Unexpected error:", e)

finally:
    print("Transaction session closed.")