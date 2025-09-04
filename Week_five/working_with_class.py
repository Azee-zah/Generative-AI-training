# class student:
#     def __init__(self, name, course, level):
#         print("Creating a new student...")
#         self.name = name
#         self.course = course
#         self.level = level
#         print(f"Student {name} has been created!")


# kemi = student("Kemi Adebayo", "Computer Science", 300)



# class patient:
#     def __init__(self, name, blood_glucose, heart_rate, blood_pressure):
#         print("Creating a new patient's records")
#         self.name = name
#         self.blood_glucose = blood_glucose
#         self.heart_rate = heart_rate
#         self.blood_pressure = blood_pressure
#         print(f"Patient {name} record has been created!")


# Tayo =patient ("Tayo Erikson", 3.54, 98, 130)


# # using init and self together:
# class NigerianStudent:
#     def __init__(self, name, state, course):
#         print("Creating student obejct...")
#         self.name = name
#         self.state_of_origin = state
#         self.course = course
#         self.student_id = self.generate_id()
#         print(f'{name} from {state} is ready!')


#     def generate_id(self):
#         import random
#         return f'UNISAIL{random.randint(1000, 9999)}'

# ayo = NigerianStudent("Ayo Daniel", "Lagos", "Street Statistics")
# tara = NigerianStudent("Tara Benson", "Ogun", "Music")

# print(ayo.name)
# print(ayo.student_id)
# print(tara.course)
# print(tara.student_id)

    
# class PhoneUser:
#     def __init__ (self, name, network):
#         print("Creating a user object...")
#         self.name = name
#         self.network = network
#         self.airtime = 0
#         print(f'{name} joined {network} network')


#     def buy_airtime(self, amount):
#         self.airtime += amount
#         return f'{self.name} now has #{self.airtime} airtime'
    


# dayo = PhoneUser("Dayo Amdalat", "MTN")
# deji = PhoneUser("Adedeji", "Airtel")

# amount = int(input("Enter your airtime amount here: "))

# # print(dayo.buy_airtime(amount))
# print(deji.buy_airtime(amount))
# print(deji.airtime)



# #ATTRIBUTES - the xtaristics of the object
# class Student:
#     def __init__ (self, name, course, level, state_of_origin):
#         self.name = name
#         self.course = course
#         self.level = level
#         self.state = state_of_origin
#         self.cgpa = 0.0

# #creating the object
# Fathia = Student ("Fathia Balogun", "Biochemistry", 200, "Ogun state")


# #accessing
# print(Fathia.name)
# print(Fathia.course)
# print(Fathia.state)

# #instance attributes
# student1 = Student("Raphina Fred", "Engineering", 400, "Lagos state")
# student2 = Student("Juwon Dele", "Medicine", 300, "Oyo state")

# print(student1.name)
# print(student2.level)
#         #Class attribute
# class Student:
#     university = "Federal University of Lagos"

#     def __init__ (self, name, course):
#         self.name = name
#         self.course = course

# # print(Student.university)
# # print(student1.university)
# # print(student2.university)

# #METHOD - what the object of a class can do
# class Student:
#     def __init__ (self, name, course, level):
#         self.name = name
#         self.course = course
#         self.level = level
#         self.cgpa = 0.0
#         self.tuition_paid = False

#     #method of the student
#     def pay_tuition(self):
#         self.tuition_paid = True
#         return f'{self.name} has paid the tuition for {self.level} level'
    
#     def register_course(self):
#         if self.tuition_paid:
#             return f"{self.name} has registered courses for {self.course}"
#         else:
#             return f"{self.name} must pay tuition fee first!"
        
    
#     def calculate_cgpa(self, grades):
#         if grades:
#             self.cgpa = sum(grades) / len(grades)
#             return f"{self.name}'s cgpa is now {self.cgpa: 2f}"
#         else:
#             return "No grades provided"
        


# Abiodun = Student("Abiodun Akinola", "Gistology", 400)
# print(Abiodun.pay_tuition())
# print(Abiodun.register_course())
# print(Abiodun.calculate_cgpa([4.2, 3.0, 4.0, 3.5]))



# # TYPES OF METHOD : 3 instance, class and static
# def pay_tuition(self):
#     return f'{self.name} has paid their tuition'  #instance method

# @classmethod
# def get_university(cls):
#     return cls.university      #class method

# @staticmethod
# def academic_calendar():                        #static method
#     return "The academic calendar runs from  September to July"



class BankAccount:
    def __init__(self, owner, bank_name, balance = 0):              #attributes
        self.owner = owner
        self.bank_name = bank_name
        self.balance = balance
        self.account_number = self.generate_account_number()


            #the methods
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"#{amount:,} has been deposited to {self.owner}'s {self.bank_name} account. New balance: #{self.balance}"
        return "Invalid deposit amount"
    

    def withdrawal(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"#{amount:,} has been withdrawn from {self.owner} acoount. New balance: #{self.balance}"
        

    def transfer(self, amount, recipient):
        if amount > 0 and amount <= self.balance:
            return f"#{amount:,} has been transfered from {self.owner} to {recipient}. Remaining balance: #{self.balance}"
        return "Transfer failed, insufficient funds"

    def check_balance(self):
        return f"{self.owner}'s {self.bank_name} account balance: #{self.balance}"


    def generate_account_number(self):
        import random
        return f"01{random.randint(10000000, 99999999)}"
    



Dara_account = BankAccount("Darasimi Addams", "TUFF Bank", 77000)  #creating

print(f"Acct Balance: {Dara_account.balance}")
print(f"Bank: {Dara_account.bank_name}")
print(f"Owner: {Dara_account.owner}")   # Attribute



