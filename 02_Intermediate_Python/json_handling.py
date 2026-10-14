# JSON Handling
# JSON stores structured data using objects, arrays, strings, numbers, etc.

import json
from pathlib import Path

file_path = Path(__file__).with_name("student.json")

# 1. Create a Python dictionary containing student information.
student = {
    "name": "Maham",
    "age": 23,
    "skills": ["Python", "AI", "Machine Learning"],
    "is_graduate": True
}

# 2. Convert a Python object into a JSON-formatted string.
json_string = json.dumps(student, indent=4)
print("JSON string:")
print(json_string)

# 3. Convert a JSON string back into a Python object.
loaded_student = json.loads(json_string)
print("\nStudent name:", loaded_student["name"])
print("Skills:", loaded_student["skills"])


# 4. Save the dictionary directly to a JSON file.
# dump() writes JSON to an open file.
with open(file_path, "w", encoding="utf-8") as file:
    json.dump(student, file, indent=4)

print("\nStudent data saved to student.json.")


# 5. Read JSON data from the file.
with open(file_path, "r", encoding="utf-8") as file:
    student_data = json.load(file)

print("Loaded student:", student_data["name"])
print("First skill:", student_data["skills"][0])


# 6. Update a value and save the changed data.
student_data["age"] = 24

with open(file_path, "w", encoding="utf-8") as file:
    json.dump(student_data, file, indent=4)

print("Updated age:", student_data["age"])