# To create days and activities pairing
# store the week days in a tuple
# ask for three days activity from user using input()
#combine the activities collected in a variable
# pairing the days and activities using dictionary comprehension
Week_days = ('Mondays', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
Defined_days = ('Mondays' , 'Friday' , 'saturday')
Actv_Mon = input("Enter your monday activity here: ")
Actv_Fri = input("Enter your friday activity here: ")
Actv_Sat = input("Enter your saturday activity here: ")
Activities = (Actv_Mon, Actv_Fri, Actv_Sat)
schedule = {Week_days: Activities  for Week_days,
             Activities in zip(Defined_days, Activities)}
print(schedule)