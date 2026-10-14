# Regular Expressions (Regex)
# The re module lets us search text for patterns.

import re

# 1. Search for a word anywhere in a string.
text = "I am learning Python programming."
match = re.search(r"Python", text)

if match:
    print("Found:", match.group())
    print("Starting position:", match.start())


# 2. Find every number in a string.
# \d means a digit; + means one or more repetitions.
text = "I completed 3 projects and studied for 20 hours."
numbers = re.findall(r"\d+", text)
print("Numbers found:", numbers)


# 3. Check whether a string begins with a pattern.
sentence = "Python is useful for AI."
match = re.match(r"Python", sentence)
print("Starts with Python:", match is not None)


# 4. Replace a word in a string.
message = "I like Java. Java is popular."
updated_message = re.sub(r"Java", "Python", message)
print("Updated message:", updated_message)


# 5. Split text using a pattern.
# This pattern splits at commas or spaces.
data = "apple,banana orange"
items = re.split(r"[, ]+", data)
print("Split items:", items)


# 6. Validate a simple email-like format.
# This is a basic learning example, not a complete email validator.
email = "maham@example.com"
email_pattern = r"^[\w.-]+@[\w.-]+\.[A-Za-z]{2,}$"

if re.fullmatch(email_pattern, email):
    print("Email format looks valid.")
else:
    print("Email format looks invalid.")


# 7. Find words that start with a capital letter.
sentence = "Ali and Sara are learning Python in Karachi."
capitalized_words = re.findall(r"\b[A-Z][a-z]*\b", sentence)
print("Capitalized words:", capitalized_words)


# 8. Replace multiple spaces with one space.
messy_text = "Python    is   fun."
clean_text = re.sub(r"\s+", " ", messy_text)
print("Clean text:", clean_text.strip())


# 9. Check whether a password contains at least 8 characters.
password = "Python123"
if len(password) >= 8:
    print("Password meets the minimum length.")
else:
    print("Password is too short.")