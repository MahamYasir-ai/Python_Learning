# CSV Handling
# CSV stands for Comma-Separated Values.
# Each row represents a record, and each column represents a field.

import csv
from pathlib import Path

file_path = Path(__file__).with_name("students.csv")

# 1. Create some student records.
students = [
    {"name": "Ali", "age": 22, "score": 85},
    {"name": "Sara", "age": 23, "score": 92},
    {"name": "Ahmed", "age": 21, "score": 58},
]

# 2. Write the records to a CSV file.
# newline="" helps avoid unwanted blank lines on Windows.
# DictWriter writes dictionaries using the column names we provide.
with open(file_path, "w", newline="", encoding="utf-8") as file:
    fieldnames = ["name", "age", "score"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()  # Write the column headings.
    writer.writerows(students)  # Write all student records.

print("Student records saved to students.csv.")


# 3. Read the CSV file as dictionaries.
with open(file_path, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    print("\nAll students:")
    for row in reader:
        print(row)


# 4. Read the file again and find students who passed.
# CSV values are read as strings, so convert score to int before comparing.
with open(file_path, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    print("\nStudents who passed:")
    for row in reader:
        score = int(row["score"])

        if score >= 60:
            print(row["name"], "-", score)


# 5. Append another student without rewriting the existing records.
with open(file_path, "a", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["name", "age", "score"]
    )
    writer.writerow({"name": "Zoya", "age": 22, "score": 78})

print("\nAdded Zoya to the CSV file.")