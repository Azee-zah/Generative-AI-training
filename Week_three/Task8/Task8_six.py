# UNILAG ADMISSION PROCESS
# collect the candidate's details : name, age, utme score, o'level results and institution choice
# store the eligibility requirements for PUTME invitation
name = input("Enter your full name as it appears on your UTME result: "). title()
age = int(input("Enter your present age here: "))
O_level = input("Do you have 5 credits at one sitting including Maths and English: ").title()
UTME_score = int(input("Enter your UTME score here: "))
institution_choice = input("Did you choose UNILAG as your first choice: ").title()
eligibility = (age >= 16) and (O_level == "Yes") and (UTME_score >= 200) and (institution_choice == "Yes")
print(f"Name: {name}\nEligible for admission process: {eligibility}")
# if (eligibility is True):
#     print(f"{name} has qualified for the UNILAG admission process")
# else:
#     print(f"{name} has not qualified for the UNILAG admission process")