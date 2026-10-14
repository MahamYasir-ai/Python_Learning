# Date and Time Handling
# Python's datetime module makes date and time calculations easier.

from datetime import date, datetime, timedelta

# 1. Get today's date and the current date and time.
today = date.today()
now = datetime.now()

print("Today's date:", today)
print("Current date and time:", now)


# 2. Create a specific date.
birthday = date(2003, 5, 15)
print("Example birthday:", birthday)


# 3. Extract individual parts of a date.
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)


# 4. Format a date using strftime().
# %d = day, %m = month, %Y = four-digit year.
formatted_date = today.strftime("%d-%m-%Y")
print("Formatted date:", formatted_date)

# You can also display the month name.
print("Month name:", today.strftime("%B"))


# 5. Convert a string into a datetime object.
date_string = "2026-10-14"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d")
print("Parsed date:", parsed_date)


# 6. Add or subtract time using timedelta.
next_week = today + timedelta(days=7)
yesterday = today - timedelta(days=1)

print("Date next week:", next_week)
print("Yesterday:", yesterday)


# 7. Calculate the number of days between two dates.
start_date = date(2026, 10, 1)
end_date = date(2026, 10, 14)

difference = end_date - start_date
print("Days between dates:", difference.days)


# 8. Compare dates.
if next_week > today:
    print("Next week's date is in the future.")
    