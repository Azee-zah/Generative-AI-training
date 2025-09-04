# Working with JSON files
import json
from pathlib import Path


workspace = Path("workspace_files")


student_data = {
    "name": "Olamide",
    "age": 16,
    "courses": ["Python", "Data Science", "Web development"],
    "grades": {"Python": "A", "Data Science": "B+", "Web development": "A-"},
    "is graduated": False
}


# to save to a json file
json_file = workspace / "student_data.json"

with open(json_file, "w", encoding="utf-8") as f:
    json.dump(student_data, f, indent=2)            #indent allows it appear neat

    print("Student data saved to JSON file!")


#to read the saved file 
with open(json_file, "r", encoding="utf-8") as f:
    loaded_data = json.load(f)

print("\n Data read from JSON file:")
print(f"Student name: {loaded_data['name']}")
print(f"Age: {loaded_data['age']}")
print(f"Courses: {",".join(loaded_data['courses'])}")
print(f"Python grade: {loaded_data['grades']['Python']}")