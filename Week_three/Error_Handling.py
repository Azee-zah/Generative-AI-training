#ERROR IN PYTHON : 3- syntax; run-time, semantics
# syntax error : i indentation error
for i in range(4):
    print(i)   # it throws error if thee is no identation before print

# missing colon or parenthesis error
if 5 > 3:    # throws error if colon is absent here
    print("Hello")

#Invalid syntax : print"Hello" : the absence of ()

#Runtime errors : your code is correct but encounters error while running
# a. Zerodivision error: dividing by zero
# b. NameError : not defining a variable before calling it
# key words to handle runtime error : try, except and finally
# try:
#     x = 10 / 2 
# print("Result:", x)

try:
    x = 10 / 0
except ZeroDivisionError:
    print("cannot divide by zero")


try:
    number = int("abc")
    result = 10 / 0
except ValueError:
    print("Invalide cpnversion to integer")
except ZeroDivisionError:
    print(" cannot divide by zero. ")

try:
    f = open("sample.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("File not found")
finally:
    print("Closing file if it was opened")

#APPLICATION OF try-except-finally blocks
balance = 5000

print("Welcome to the ATM")
amount = input("Enter amount to withdraw: ")

try:
    amount = float(amount)
    if amount > balance:
        raise ValueError("Insufficient funds")
    balance -= amount
    print("Withdrawal successful. New balance: #", balance )

except ValueError as e:
    print("Error:", e)

except Exception as e:
    print("Unexpected error:", e)

finally:
    print("Transaction session closed")