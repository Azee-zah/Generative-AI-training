#creating tuple : can be using parenthesis or without parenthesis
fruits = ("apple" , "banana" , "cherry")
print(fruits)   # tuples with multiple elements and using parenths

numbers = 1, 2, 3, 4
print(numbers)
outfit = "bottega" , "jeans" , "socks"
print(outfit)

#single_item tuple: this must include a comma
single_item = ("apple",)
print(single_item)
print(type(single_item))

#using the tuple():  tuple constructor
fruits_list = ["apple" , "banana" , "cherry"]
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)    # this converts list to tuple

#xteristics of tuple
colors =("red" , "green" , "blue")
print(colors[1])     #a tuple is ordered
#colors[1] = "yellow"  # this pulls error cause a tuple is immutable

numbers = (1, 2, 2, 3)
print(numbers)  # tuple allows for duplicate

mixed = ("apple" , 1, 3.14, True, False)
print(mixed)   # tuple allows mixed data

nested = (("a" , "b"), (1, 2))
print(nested)  # we can have a nested tuple too

# Tuple Operations
fruits = ('apple' , 'banana' , 'cherry')
print(fruits[1])
print(fruits[-1])   # you can index a tuple

print(fruits[0:2])
print(fruits[0:3])
print(fruits[::-1])
print(fruits[:-1])
print(fruits[-1::])   # slicing tuple

tuple1 = (1, 2)
tuple2 = (3, 4)
result = tuple1 + tuple2
print(result)   # concatenation in tuple

nums = (1, 2)
print(nums * 3)  #repition in tuple

fruits = ('apple' , 'banana' , 'cherry' , 'coocnut' , 'mango')
print('banana' in fruits)
print('grape' in fruits)
print('grape' not in fruits)  #membership

for fruit in fruits:
    print(fruit)   #iteration

person = ("John", 25, "Nigeria")
name, age, country = person
print(name)
print(age)
print(country)   #unpacking tuple

#Tuple methods : tuples have two methods; the convert list to tuple and the built_in fnc with tuple
#converting between list and tuple
t = (1, 2, 3)
to_list = list(t)
to_list.append(4)
print(to_list)   #converting tuple to list and appending a new element

#converting list to tuple
t = tuple(to_list)
print(t)

#built-in function
nums = (4, 1, 7, 3)
print(len(nums))   #length of elements in the tuple
print(max(nums))
print(min(nums))
print(sum(nums))
