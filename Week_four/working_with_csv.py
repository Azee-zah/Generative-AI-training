import csv
from pathlib import Path


workspace = Path("workspace_files")
csv_file = workspace / "student.csv"

students = [
    ["Name", "Age", "Course", "Grade"],   # Header row
    ["Precious", 20, "Python", "A"],
    ["Favour", 22, "JavaScript", "B+"],
    ["Ore", 21, "Python", "A-"],
    ["Susan", 23, "Data Science", "A"]
    
]

# write data to CSV file
with open(csv_file, "w", newline="",  encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(students)   #write rows at once

print("Student data written  to CSV file!")

#Read the CSV file
print("\nReading CSV file:")

with open (csv_file, "r", encoding="utf-8") as f:
    reader = csv.reader(f)

    for row_number, row in enumerate(reader):
        if row_number == 0:   # haeder
            print(f"Headers: {'|'.join(row)}")
            print('-' * 40)
        else:
            name, age, course, grade = row
            print(f"{name} ({age}years) - {course}: {grade}")



