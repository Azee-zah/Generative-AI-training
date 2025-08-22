seat_nums = set(range(1,51))
print(input("avalable seat:", seat_nums))
book_seat = int(input("Book a seat number here: "))
seat_nums.remove(book_seat)
# print("Removed:", removed)
# remaining = seat_nums
print(seat_nums)