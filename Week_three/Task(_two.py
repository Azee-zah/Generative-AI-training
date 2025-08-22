# CREATING A UNIQUE VOTERS REGISTRATION SYSTEM
voters = set()
while True:
    names = input("Enter your name here to vote (type exit to quit): ").title()
    if names.lower() == 'exit':
        print("Goodbye!")
        break
    if names in voters:
        print(f"Warning {names} voted already")
    else:
        voters.add(names)
        print(f"Hello, {names} you have voted ")

nums_voter = len(voters)
print(nums_voter)


