#set in python
#lets create sets
fruits = {"apple" , "banana" , "mango"}  #set uses curly braces
print(fruits)    

#can also use the set () constructor
numbers = set([1, 2, 3])
print(numbers)   #this prints out in curly braces
numbers = set((1, 2, 3))    #works same way
print(numbers)

#creating empty set : to achieve this, we use ()
empty_set = set()
print(empty_set)

#sets doesnt support duplicates
#converting a string to set, it removes the duplicates automatically
letters = set("mississippi")
print(letters)  #this prints without repeating duplicated letters

#Sets operations
colors = {"red" , "blue"}
colors.add("green")
print(colors)  #adding elements to the set

colors.remove("blue")  #remove throws error if such element is not in the set
colors.discard("yellow")  #discard does not throw error even when the element is not preentt in the set
print(colors)
#pop() to remove an element from the set
#but this seems like you cant control what it pops
colors = {"red" , "blue" , "green"}
removed = colors.pop()
print("Removed:", removed)
print("Remaining:", colors)

clothing = {"shoe" , "skirt" , "socks" , "sneakers"}
removed = clothing.pop()
print("Removed:", removed)
print("Remaining:", clothing)

snacks = {"buns" , "puff-puff" , "sausage"}
removed = snacks.pop()
print("Removed:", removed)
print("Remaining:", snacks)

cars = {"escalade" , "RX350" , "G-wagon" , "camry"}
removed = cars.pop()
print("Removed:", removed)
print("Remaining:", cars)

#clear a set
cars.clear()
print(cars)

#mathematical operations in set
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1 | set2)
print(set1.union(set2))
print(set2.union(set1))  #using union in set

print(set1 & set2)
print(set1.intersection(set2))  #using intersection in set

print(set1 - set2)
print(set1.difference(set2))   #difference in set
print(set2 - set1)

print(set1 ^ set2)
print(set1.symmetric_difference(set2))
print(set2 ^ set1)   #symmetric_difference in set

# working with sets
#collecting unique visitors to an event
visitors = set()
#to add the visitors
visitors.add("chinedu")
visitors.add("Aisha")
visitors.add("chinedu")
print(visitors)   #works the same way as the command below
print("Visitors:", visitors)

#to find out if a visitor attends or not: using if and else
name = "Aisha"
if name in visitors:
    print(f"{name} attended the event")
else:
    print(f"{name} did not attend the event")

