# explaining the output
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"{num1} == {num2} : {num1 == num2}")
# the output implies if first number is the same as second number, then it should return true
#but in a case where the first number is not the same as the second number, it returns false

print(f"{num1} != {num2} : {num1 != num2}")
# the output returns True if the first number is not the same as the second number
# but returns False if the first number is the same as the second number
# this is because != means 'is not equal to'

print(f"{num1} > {num2} : {num1 > num2}")
# the output returns False when the first number is not greater than the second number
# but in a case where the output is True, it shows the first number is greater than the second

print(f"{num1} < {num2} : {num1 < num2}")
# the output returns True when the first number is smaller than the second
# when the output returns False, it shows the first number is bigger than the second

# The 3 case scenarios where the program can be applied :
# 1. it can be used to track a patients's heart rate
# 2. it can be used to compare prices from different stores
# it can be used to monitor a student grade overtime

# Writing the code to track a patient's heart rate
exercising_heart_rate = int(input("Enter your recorded heart rate while exercising: "))
resting_heart_rate = int(input("Enter  recorded heart rate at rest: "))
print(f"{exercising_heart_rate} == {resting_heart_rate} : {exercising_heart_rate == resting_heart_rate}")