while True:
    name = input("Enter your full-name here: ").title()
    if name == 'Stop':
        print("End of registration")
        break
    citizenship = input("What is your nationality: ").title()
    enrollment = input("Are you a full-time undergraduate in a Nigerian university? ").title()
    other_scholarships = input("Are you a beneficiary of any oil and gas scholarship? ").title()
    academic_qualification = input("Do you have 5 distinctions in relevants WAEC subject including Math and Engliish? ").title()
    # eligibility = (citizenship == "Nigerian") and (enrollment == "Yes") and (other_scholarships == "No") and (academic_qualification == "Yes")
    # print("Eligibility", eligibility)



    if citizenship == "Nigerian":
        if enrollment == "Yes":
            if academic_qualification == "Yes":
                if other_scholarships == "No":
                    print(f"{name}, you are Eligible for this scholarship")
                else:
                    print(f"{name}, You are not Eligible.")

## experimented nested if

    
    


