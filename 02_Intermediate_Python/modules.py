# Python Modules
# Import modules when you want to reuse existing functionality.

# 1. math provides mathematical functions and constants.
import math

print("Square root:", math.sqrt(64))
print("Factorial:", math.factorial(5))
print("Pi:", math.pi)


# 2. random generates pseudo-random values.
import random

print("Random integer:", random.randint(1, 100))

colors = ["red", "blue", "green"]
print("Random color:", random.choice(colors))


# 3. statistics calculates common statistical values.
import statistics

scores = [70, 80, 80, 90, 100]
print("Mean:", statistics.mean(scores))
print("Median:", statistics.median(scores))


# 4. Import a specific function instead of the entire module.
from datetime import date

today = date.today()
print("Today's date:", today)


# 5. Aliases give modules shorter names.
import calendar as cal

print("October 2026 calendar:")
print(cal.month(2026, 10))