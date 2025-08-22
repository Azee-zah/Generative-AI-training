#strings in python
#step1 : working with single quote
#name = 'Ada'
#step2 : using double quote
#greetings = "Hello"
#step3 : using triple quotes for multi-line strings
#story = '''Once upon a time,
#there was a programmer named Ada.'''
# numbers and symbols in form of strings
#password = "p@ssword123"

#working with indexing
word = "python"
print(word[0])
print(word[-1])
print(word[-2])
print(word[-6])
print(word[4])

#working with slicing
word = 'Pythonlanguage'
# print(word[0:4])
# print(word[2:])
# print(word[0:])
# print(word[:3])
# print(word[::2])
# print(word[::-1])
print(word[::-2])
# print(word[::-3]) # this 
# print(word[:])
# print(word[::])
print(word[:-2])

# String Concatenation and Repetition
a = "hello" 
b = "World"
c = "I am here"
print(a + " " + b + " " + c)  # concatenation

word = "Hi! "
print(word * 3)
word = "Hi!"
print(word * 4)     #repetition

#string seraching and checking
text = "Python programming"
print("Python" in text)
print("Java" not in text)
print("econs" in text)      #membership

text = "Hello World"
print(text.find("o"))
print(text.find("l"))
print(text.rfind("l")) #find and rfind

text = "Hello World"
print(text.index("World"))
print(text.index("Hello"))
print(text.index("orld"))
print(text.index("Hello"))
print(text.index("llo"))
print(text.rindex("llo"))       #index and rindex

filename = "data.csv"
print(filename.startswith("data"))
print(filename.endswith("data")) #startswith and endswith

#string Methods
