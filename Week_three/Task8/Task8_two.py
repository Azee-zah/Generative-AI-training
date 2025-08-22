# COMMENTING THE CODE
# collect the user details: name, age and score
# ensure you use appropriate datatype like int for score
# define the eligibility criteria and store in a variable : use the logical and comparison operator
# display the output in a neat format on seperate lines  #hint : use escape sequence \n
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# score = int(input("Enter your test score: "))

# eligibility = (age < 18) and (score > 70)
# print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")

# THE CASE : SCHOLARSHIP ELIGIBILITY
#Ask the user for their info: citizenship, enrollment, other scholarship and academic qualification
citizenship = input("What is your nationality?: ").title()
enrollment = input("Are you enrolled as a full-time undergraduate in a reputable Nigerian university? "). title()
other_scholarships = input("Are you a benificiary of any other form of scholarship: ").title()
academic_qualifications = input("how many distinctions do you have in your relevant subjects: ")

eligibility = (citizenship == "Nigerian") and (enrollment == "Yes") and (other_scholarships == "No") and (academic_qualifications == "5")
print(f"Nationality: {citizenship}\nEnrollment: {enrollment}\nother_benefits: {other_scholarships}\nAcademic_qualification: {academic_qualifications}\nEligible: {eligibility}")