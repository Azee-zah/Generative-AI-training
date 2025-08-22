# operators in python : operators performs operations on variables and values
# 3 major operators : comparison, assignment and logical
# The comparison operators : are used to compare two values, output is True or False
# a = 10
# b = 20
# print(a==b)  # outputs false
# print(a != b) #outputs True
# print(a>b)
# print(a < b)
# print(a >= 10)
# print(b <= 25)

# # case example using student Exam result
# score = 75
# print(score >= 50) # True
# print(score < 50)  #false
# print(score == 100) #returned false

# Assignment Operators : used to assign values to variables
# can also combine operators like += 
x = 10
print("Initial value:", x)  #prints 10
x += 5
print("After x +=5:", x)  #prints 15
x -= 2
print("After x -=2:", x)  #this prints 13
# print("Initial value-=2:", x)
x *= 3
print("After x *=3:", x)  #multiplies 13 by 3
x /= 4
# print("Before x /= 4:", x)  #9.75
print("After x /= 4:", x)  #same thing: divied 39 by 4
x %= 3
print("After x %= 3:", x)  #prints the remainder from 9.75 divided by 3

x = 4
x **= 2
print("After x **= 2:", x)
x //= 3
print("After x //=3:", x)

#CASE EXAMPLES
balance = 1000
deposit = 200
withdraw = 150

balance += deposit
balance -= withdraw
print("Updated Balance:", balance)

#Logical Operators : and or not
# used to combine conditional statements
# works with boolean values
x = 10
y = 20
print(x > 5 and y > 15) # the and operator
print(x < 5 or y > 15) #the or operator
print(not(x == 10))

# Scholarship Eligibility  (For case example)
age = 17
score = 85
eligible = (age < 18) and (score > 80)
print("Scholarship eligible:", eligible)  #prints true
#Event access
age = 22
has_ticket = False
can_enter = (age >= 18) and (has_ticket and age < 25)
print("Access Granted:", can_enter)



