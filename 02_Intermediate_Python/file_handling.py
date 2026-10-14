# File Handling
# Files let us save information even after a program stops running.

from pathlib import Path

# Build the path to sample.txt in this script's own folder.
file_path = Path(__file__).with_name("sample.txt")


# 1. Write text to a file.
# "w" creates the file or replaces its existing contents.
with open(file_path, "w", encoding="utf-8") as file:
    file.write("Hello, Python!\n")
    file.write("I am learning file handling.\n")

print("File written successfully.")


# 2. Read the entire file.
# "r" opens a file for reading.
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

print("\nFile contents:")
print(content)


# 3. Append new text without deleting the existing content.
# "a" adds text at the end of the file.
with open(file_path, "a", encoding="utf-8") as file:
    file.write("This line was added later.\n")


# 4. Read the file one line at a time.
with open(file_path, "r", encoding="utf-8") as file:
    print("Reading line by line:")
    for line in file:
        print(line.strip())  # strip() removes the newline at the end.


# 5. Check whether a file exists before trying to read it.
if file_path.exists():
    print("\nFile size:", file_path.stat().st_size, "bytes")
else:
    print("The file does not exist.")