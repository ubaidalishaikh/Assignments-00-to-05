# Problem Statement

# Use Python to calculate the number of seconds in a year, 
# and tell the user what the result is in a nice print statement that looks like this (of course the value 5 should be the calculated number instead):

# Solution

DAYS_IN_YEAR = 365
HOURS_IN_DAY = 24
MINUTES_IN_HOUR = 60
SECONDS_IN_MINUTE = 60

# Calculate total seconds in a year
seconds_in_year = DAYS_IN_YEAR * HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE

print(f"There are {seconds_in_year:,} seconds in a year!")
