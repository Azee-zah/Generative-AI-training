#store name is a loop, phone number in another loop
# using zip() to combine the tuples
# dict() converts to dictionary

names = ('Tope', 'Richard', 'Olamide')
contacts = ('+2340987', '+23466578', '+23490987')
contact_loop = dict(zip(names, contacts))
print(contact_loop)
ask_user = input("Enter a name: ")
print(contact_loop.get('Tope'))  #this retrieves Tope's contact

