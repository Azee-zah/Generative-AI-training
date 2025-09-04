#User defined functions
def greet():                #defining a function
    print("Hello, welcome to AI fellowship!")

greet()
greet()
greet()


def greet(name):            #the argument in parenths
    print("Hello", name, "welcome to Python learning")

greet("Class rep")   #when calling, -the parameter
greet("Ridwan")

#return, print and yield
def greet(name):
    print("Hello", name)

result = greet("Esther")

print("Result:", result)

def add(a, b):
    return a + b

result = add(4, 6)
print("The sum is:", result)


def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for number in count_up_to(5):
    print(number)