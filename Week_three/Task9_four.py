student = {}
while True:
    full_name = input("Enter your full-name here: ").title()
    if full_name == 'Stop':
        print("End of admission registration ")
        break
    age = int(input("Enter your current age: "))
    inst_choice = input("Is UNILAG your first choice: ").title()
    utme_score = int(input("Enter your JAMB score: "))
    o_level1 = input("Is your O level result in one sitting? ").title()
    o_level2 = input("Do you have 5 credits in relevant subject including Math and English ").title()
    if age >= 16:
        if utme_score >= 200:
            if o_level1 == "Yes":
                if o_level2 == "Yes":
                    if inst_choice == "Yes":
                        print(f"{full_name} has qualified for the UNILAG P-UTME screening process")
                    else:
                         print(f"{full_name} is not qualified for the UNILAG p-UTME screening process ")
    # eligibility = (age >= 16) and (utme_score >= 200) and (o_level1 == "Yes") and (o_level2 == "Yes") and (inst_choice == "Yes")
    # print (f"{full_name} has qualified for the UNILAG P-UTME screening process")



    #ADMISSION PROCESS
    cut_off = int(input("Enter the P-UTME screening score: "))
    if cut_off >= 200:
        print(f"Congratulations!!. {full_name} has been offered admission")
    else:
        print(f"Sorry! {full_name} has not been offered admission!")



