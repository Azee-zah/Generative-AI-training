import first
import second

# using the functions in your first
print("=== Math Functions ===")
print("5 + 3=", first.add(5, 3))
print("10 - 4=", first.subtract(10, 4))
print("6 * 7=", first.multiply(6, 7))
print("20 / 5=", first.divide(20, 5))


# using function in the second file
print("\n=== String Functions ===")
print(second.greet("Ridwan"))
print("The reverse of 'Python' =", second.reverse_string("Python") )
print("Character count in sentence =", second.count_characters("Python modules are powerful"))
print("Word count in sentence =", second.count_words("Python moduls are powerful"))