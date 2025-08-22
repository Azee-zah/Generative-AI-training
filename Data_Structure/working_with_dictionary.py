# # The syntax of a dictionary
# #dictionary_name = {key1: value1, key2: value2}  #the key is the word, value is the meaning
# #creating dictionary
# student = {
#     "name": "Ada",
#     "age": 20,
#     "course": "Computer Science"
# }
# print(student)
# # we can also use dict() constructor
# student_info = dict(name="John" , age=23, course="maths")
# print(student_info)

# # to create an empty dictionary
# empty_dict = {}
# print(empty_dict)
# empty_dict1 = dict()
# print(empty_dict1)

# # Dictionary comprehension
# # The syntax: {key_comprehension: value_comprehension for item in iterable if condition}
# squares = {x: x**2 for x in range(1, 6)}  #a dictonary of numbers and its squares
# print(squares)

# #with condition : this is conditioning x the key_comprehension
# # this to print out even numbers and its cubes
# evens_cube = {x: x**3 for x in range (1, 10) if x % 2 == 0}
# print(evens_cube)

# #from existing dictionary
# students = {"Ada": 85, "John": 40, "Musa": 65}
# passed_students = {name: score for name, score in students.items() if score >= 50}
# print(passed_students)

# # Using string keys
# names = ["Ada", "John", "Musa"]
# lengths = {name: len(name) for name in names}
# print(lengths)

# to access dictionary items
# define the dictionary
student = {"name": "Ada", "age": 20, "course": "Computer science"}
# using the key to access the dictionary item
print(student["name"])

# using get() method
print(student.get("age"))
# in the get method, it does not throw an error even when the key is missing

# Modifying dictionaries : to remove, change item or to add item
student["age"] = 21
print(student)   # this changes the age of the student

student["grade"] = "A"   # this add a new key-value to the dictionary
print(student)
#to remove items from the dictionary
# this can be done in four ways : pop(), popitem(), del , clear()
# student.pop("grade")  # this removes the grade from the dictiionary
# print(student)

# student.popitem()  # this removes the last inserted key-value
# print(student)

del student["course"]  #using the del keyword
print(student)
student.clear()
print(student)

# Dictionary methods : 4 methods
person = {"name": "Emeka" , "age": 23}
print(person.keys())  #to pull the keys in dictionary out
print(person.values()) #to pull the values in the dictionary out
print(person.items())  #to pull the k-v pair
print(person.update({"age": 31 , "city": "Lagos"})) #to update the dictionary
print(person)

#Nested dictionary
students = {
    "student1": {"name": "Ada" , "age": 20},
    "student2": {"name": "John" , "age": 22}
}
print(students["student1"]["name"])  #this help to accesss the name of student1

#Loop through dictionaries : keys , values , k-v pairs
student = {"name": "Ada" , "age": 23, "course": "Computer science"} #defining the dict
for key in student:
    print(key)  #loop through key
for value in student.values():
    print(value) # loop through values
for key, values in student.items():
    print(f"{key}: {values}")  #loop through k-v pairs

# storing a a student's biodata
student = {
    "name": "Chinedu",
    "age": 23,
    "department": "Engineering",
    "subjects": ["Maths" , "Physics" , "Chemistry"],
    "is_full_name": True
}
print(f"Name: {student['name']}")  #this printed the student name
print(f"Subject: {','.join(student['subjects'])}")  # printed the subjects separated by commas




