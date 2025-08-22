#creating and manipulating strings
#use upper and lower to change case 
name = "Ayooola Esther"
print(name.upper())  #upper case
sentence = "python is amazing"
print(sentence.title())  #title case
imagination = "REMAIN WILD"
print(imagination.lower())  #lower case
text = "    Abuja    "
print(text)
print(text.strip())    #strip

message = "I love Java"
print(message.replace("Java" , "Python")) #replace
message = "I Love You"
print(message.replace("You" , "Me"))

text = "Hello ABEOKUTA"
print(text.swapcase())
word = "positiVitY"
print(word.swapcase())  #swapcase
text = "        Nigeria"
print(text.lstrip())  #lstrip
word = "Nigeria       "
print(word.rstrip())  #rstrip

#split
fruits = ("mango orange banana")
print(fruits.split())
states = "Abia Ondo Jigawa Oyo Lagos"
print(states.split(","))
amount = "2000000"
print(amount.split(","))
#rsplit
text = "one,two,three,four,five"
print(text.rsplit())
text = "one two three four"
print(text.rsplit())
text = "one two three four"
print(text.rsplit(",", 2))

foods = "yam\nSpag\nPotatoes"
print(foods.splitlines())
#join
words = ["I", "Love" , "Python"]
print(" ".join(words))
# center
text = "Python"
print(text.center(20, "-"))
print(text.center(10, ","))

#ljust and rjust
text = "python"
print(text.ljust(10, "?"))
print(text.rjust(10, "#"))
