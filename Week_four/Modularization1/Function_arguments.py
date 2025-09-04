# TYpes of arguments
def introduce(name, track):             #Positional arguments
    print("MY name is", name)
    print("I am learning", track, ".")


introduce("Dara" , "AI Engineering")
introduce("AI Engineering" , "Dara")


#Keyword Arguments
def introduce(name, track):
    print("My name is", name)
    print("I am learning", track, ".")

introduce(name = "Ngozi", track = "AI Engineering")

introduce(track = "AI Engineering", name = "Ngozi")


#Default Arguments
def introduce(name, track = "AI Engineering"):
    print("MY name is", name)
    print("I am learning", track, ".")

introduce("Paul")   #without specifying

introduce("Tunji Paul", track = "AI Development")


#non_keyword arguments (*args) - tuple
# keyword arguments (**kwargs) - dict

def add_numbers(*args):
    total = 0
    for num in args:
        total += num
        print("Sum:", total)

add_numbers(2, 4, 6)
add_numbers(10, 20, 30, 40, 50)

def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student_details(name = "Paul", track = "AI Engineering", interest="Block Chain")


# A STUDENT BOOTCAMP PROFILE
def participant_profile(name, age, track="AI Development", *skills, **extra_info):
    """
    Generate a profile for a bootcamp participant using different types of arguments
    """
    profile = f"\n---Bootcamp Participant Profile ---\n"
    profile += f"Name: {name}\n"
    profile += f"Age: {age}\n"
    profile += f"Track: {track}\n"

    # skills from *args
    if skills:
        profile += "Skills: " + ", ".join(skills) + "\n"
    else:
        profile += "Skills: Not yet specified\n"

    #Extra info (from **kwargs)
    if extra_info:
        profile += "Additional Info:\n"
        for key, value in extra_info.items():
            profile += f" - {key.capitalize()}: {value}\n"

    return profile   # to store and re-use



print(participant_profile("Peter", 24))    # positional arguments

print(participant_profile("David", 27, "Data Science", "Python", "SQL", "Machine Language"))

print(participant_profile(
    "Sophia", 30, "Cybersecurity"
    "Networking", "Ethical Hacking", "Python",
    interest="Blockchain", city="Shagamu", phone="08123456789"
))