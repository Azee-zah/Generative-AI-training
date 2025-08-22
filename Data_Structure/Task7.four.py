# Creating a unique membership registration
# collect the names using input()  .split () helped split so all are not combined as one
# convert to set {} or set()
# dictionary k-v pairing name as key and length len() as values 
user_name = input("Enter 3 your names: ").split()
converted_name = set(user_name)
members_reg = {user_name: len(user_name) for user_name in converted_name }
print(members_reg)
