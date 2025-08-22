#CONTROL FLOW IN PYTHON
# 3 methods : conditionals , Loop and Control
#CONDITIONAL STATEMENTS
#if statement: works when the condition is true
age = 20
if age >= 18:
    print("You are eligible to vote")

#if-else statement: two conditions
wallet = 400
price = 500
if wallet >= price:
    print("Purchase successful")
else:
    print("Insufficient balance")

#If-elif-else : this is used for multiple conditions
score = 85
if score >= 70:
    print("Grade A")
elif score <= 50:
    print("Grade B")
else:
    print("Grade C")

# Nested If : houses if in if
age = 20
citizen = True
if age >= 18:
    if citizen:
        print("You can vote")
    else:
        print("You need to be a citizen to vote!")
else:
    print("Too young to vote")

#LOOP : we have for loop and while loop
#for loop : it iterates through each element in a LIST
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f'I love {fruit}')

coordinates = (0.34654, -0.48585, 0.57477)  #in a tuple
for point in coordinates:
    # print(f"Point: {point}")
    print(f"Point: {point}")

student = {"name": "Tunde", "age": 16, "grade": "A"}  # for a dictionary
for key, value in student.items():
    print(f"{key}: {value}")


word = "PYTHON"   # for a string
for char in word:
    print(char)


#while loop: repeat a block of condition as long as condition is true. while loop is condition based
# when the condition becomes false, the loop stops
count = 1
while count <= 5:
    print("Number:", count)
    count += 1   #this is the condition

# incrementing with while
num = 1
while num <= 10:
    print(num, end=" ")  # this prints on a single line and separates using a space
    num += 1   # the condition

#decrementing with while
timer = 10
while timer > 0:
    # print(timer, end=" ")
    print("countdown:", timer)
    timer -= 1


# while with input
password = ""
while password != "python123":             #keep asking you enter the correct code
    password = input("Enter the password: ")
print("Access Granted")

ussd_code = ""
while ussd_code != "*123#":
    ussd_code = input("Enter the ussd code here: ")

print("Welcome back!, do your transactions here")


# WHILE TRUE
while True:
    name = input("Enter your name (type 'exit' to quit): ")
    if name.lower() == "exit":
        print("Goodbye")
        break
    print(f"Hello, {name}")

#THE LOOP CONTROL STATEMENTS : break, continue and pass
for num in range(1, 10):
    if num == 5:
        break
    print(num)       # break

for num in range(1,6):
    if num == 3:
        continue
    print(num)      # for continue

for num in range(1,6):
    if num == 3:
        pass
    else:
        print(num)

while True:
    print("\nMenu:")
    print("1. Say Hello")
    print("2. Goodbye")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Hello")
    elif choice == "2":
        print("Goodbye")
    elif choice == "3":           #the break here exited the program while other option run then start from the beginning since there is no specification of break after their own option
        print("Exiting program...")
        break
    else:
        print("Invalide choice. Try again")


#while True for validation
while True:
    age = input("Enter your age here: ")
    if age.isdigit():
        print(f'Your age is {age}')
        break
    else:
        print("Invalid input. Please enter a number")


secret = "python"      #try making a guess

while True:
    guess = input("Guess the secret word: ")
    if guess.lower() == secret:
        print("Correct! You guessed the word right.")
        break
    else:
        print("Wrong! Try again.")
        # break      # you can use break multiple times in a code


balance = 1000
while True:
    print("/nMenu")
    print("1. Check balance")
    print("2. Withdraw")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print(f'Your balance is: {balance}')
    elif choice == "2":
        amount = int(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            print(f"Withdrawal successful. New balance: {balance}")
        else:
            print("Insufficient funds.")
    elif choice == "3":
        print("Thank you for using our ATM. Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
    
