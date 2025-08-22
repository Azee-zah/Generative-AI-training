# Creating a super Market price list
# use the input() to collect price from users
# create the dictionary
BodyLotion_price = float(input("Enter the lotion price: "))
Haircream_price = float(input("Enter the cream price: "))
Shampoo_price = float(input("Enter the shampoo price: "))
Moisturizer_price = float(input("Enter the moisturizer price: "))
Items = ["BodyLotion", "HairCream" , "Shampoo" , "Moisturizer"]
Market_list = {
    "Body_lotion": BodyLotion_price,
    "Hair_cream" : Haircream_price,
    "Shampoo": Shampoo_price,
    "Moisturizer": Moisturizer_price
}
print(f"Body_lotion: {BodyLotion_price}\nHair_cream: {Haircream_price}\nShampoo: {Shampoo_price}\nMoisturizer: {Moisturizer_price}")
print(Market_list.update({"Shampoo": 90000}))
print(Market_list.keys())