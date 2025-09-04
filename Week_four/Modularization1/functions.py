# def greet(name):
#     print("Hello", name)

# # girls = input("Tell me your name")
# # greet(girls)

# # result = greet("Esther")
# # print("Result", result)

# def add(a, b):
#     return a + b

# person = {
#     "Name": "Ola",
#     "Age": 21,
#     "Subject": "English"
# }
# for key in person:
#     print(key)

# for values in person.values():
#     print(values)

# for key, values in person.items():
#     print(f"{key}: {values}")

# def email_slicer(email):
#     if "@" in email and "." in email:
#      username, domain = email.split("@")
#      return username, domain
    

# mail = input("Enter your email address: ").strip() 


email = input("Enter your email address ").strip()

if "@" in email and "." in email:
    username, domain = email.split("@")

    print(f"Username: {username}")
    print(f"Domain: {domain}")
else:
    print("Invalid email")

