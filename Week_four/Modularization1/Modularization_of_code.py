for i in range(3):
    print(i)                #range()

names = ["Esther", "Precious", "Kennie"]
scores = [85, 90, 75]
for n,s in zip(names, scores):              #zip()
    print(n, "scored", s)


nums =[1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))                       #map()
print(squared)

even_nums = list(filter(lambda x: x % 2 == 0, nums))     #filter()
print(even_nums)


# even_nums = {x: x % 2 == 2 for x in nums}
# print(even_nums)

name1 = input("Enter first student name: ")
score1 = int(input("Enter score for " + name1 + ": "))

name2 = input("Enter second name: ")
score2 = int(input("Enter the score for " + name2 + ": "))

name3 = input("Enter the third name: ")
score3 = int(input("Enter the score for " + name3 + ": "))      #collecting data

names = [name1, name2, name3]
scores = [score1, score2, score3]                   #store in a list

print("\nStudent Data:")
for index, (n, s) in enumerate(zip(names, scores)):
    print(f"{index + 1}. {n} - {s}")                #displaying the data


total = sum(scores)
average = round(total / len(scores), 2)
highest = max(scores)
lowest = min(scores)

print("\nPerformance Summary:")
print("Total Score:", total)
print("Average Score:", average)
print("Highest Score:", highest)
print("Lowest Score:", lowest)          # Summary in built-in

ranked = sorted(zip(scores, names), reverse=True)
print("\nRanking:")
for rank, (score, name) in enumerate(ranked, 1):
    print(f"{rank}. {name} - {score}")   #for ranking

print("\nData Type Checks: ")
print("Type of names:", type(names))
print("Type of scores:", type(scores))
print("ID of names list:", id(names))
print("ID of scores list", id(scores))          #checkking data type

passing = list(filter(lambda s: s >= 50, scores))
print("\nPassing Scores:", passing)   #filter passing students (>=50)

upper_names = list(map(lambda n: n.upper(), names))
print("Uppercase Names:", upper_names)

print("\nHelp on len(): ")
help(len)


