# STATE INVENTORY UPDATE
store = {"Toyota": 10, "Audi": 22, "Lexus": 12, "Honda": 8}
item_demand = input(f"Enter the item you would like to get from the {store}: ").title()
quantity_demand = int(input(f"Enter the quantity of {item_demand} you would like: "))
print(f"Before purchase: {store}")
store[item_demand] -= quantity_demand
print(f"After Purchase: {store}")
# store[item_demand] -= quantity_demand
# print(store)



