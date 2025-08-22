#collecting guests name
# to prevent duplicate convert to set
#use sorted() for alphabetical order
seminar_guest1 = input("Enter your name if you are attending the seminar: ")
seminar_guest2 = input("Enter your name if you are attending the seminar: ")
seminar_guest3 = input("Enter your name if you are attending the seminar: ")
Seminar_guests = {seminar_guest1, seminar_guest2, seminar_guest3}
print(sorted(Seminar_guests))

