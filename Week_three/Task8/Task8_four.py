# STUDY RECORD
# creating an empty dictionary
# collect user details: name and age
# store em
# create a list of scores
student = {}
name =input("Tell us your full name: ")
age = int(input("Tell us your age: "))
scores = [50, 60, 85]

student = {
    "Name": name,
    "Age": age,
    "Scores": scores
}
average_score = sum(scores) / len(scores)  # this is defining the average score
Passed = (average_score >= 50)
Teenager = (age > 13) and (age <= 18)
print(f"Name: {name}\nAge: {age}\nScores: {scores}\nPassed: {Passed}\nTeenager: {Teenager}")

