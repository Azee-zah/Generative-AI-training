# creating a list : 2 ways
empty_list = []
print(empty_list)  #using the square bracket

Empty_list = list()
print(Empty_list)  #using the list() constructor

#creating a list with elements in it
numbers = [1, 2, 3, 4,5]
print(numbers)   #list of integers

fruits = ["apple" , "banana" , "cherry"]
print(fruits)  #list of strings

mixed_list = ["Alice" , 25, 5.8, True]
print(mixed_list)   #list of mixed datatypes
mixed_list2 = ['Alice' , 21, 4.5, False]
print(mixed_list2)   #list of mixed datatype

#converting other datatypes into a list
welcome = "hello"
chars = list("hello")
print(chars)    #string to list
practise = "welcome to the resolution, nothing is compared to graeter acheivements"
practise_list = list(practise)
print(practise_list)

my_tuple = (10, 20, 30)
list_from_tuple = list(my_tuple)
print(list_from_tuple)  #tuple to list

numbers_range = list(range(5))
print(numbers_range)    #range to list

#creating a nested list
#nested list : is a list that contains other list as its element
matrix = [[1,2], [3,4], [5,6]]
print(matrix)   #matrix-like list
#to access elements in a list
print(matrix[0])
print(matrix[0][1])

#exploring the xteristics of a list
fruits = ["mango" , "orange" , "banana"]
print(fruits)
print(fruits[0])
print(fruits[2])    #it follows a ordered form

items = ["rice" , "beans" , "yam" , "rice"]
print(items)    # it allows duplicate elements

numbers = [1,2,3]
numbers[1] = 20
print(numbers)  #mutable : can change the elements in the list

mixed = [10, "Nigeria" , 3.147, True]
print(mixed)  # can contain different datatypes

nested_list = [[1,2], ["a" , "b"]]
print(nested_list)
print(nested_list[0])
print(nested_list[1][0])   # can be nested

names = ["Ada"]
names.append("Bola")
names.append('Zainab')
print(names)        #dynamic size: append helps you add a new element to the list

#squares of numbers 0-4
square = [x**2 for x in range(5)]
print(square)
#squares of number 0-12
square = [x**2 for x in range(13)]
print(square)

#for even numbers
even_numbers = [y for y in range(13) if y % 2 == 0]
print(even_numbers)
