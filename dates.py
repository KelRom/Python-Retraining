from datetime import date
from datetime import datetime
from datetime import timedelta

# Date Objects
# Getting todays date
todays_date = date.today()
print(f"Today's date is {todays_date}")

# Getting individual components
print("Date Componenets: ", todays_date.day,
      todays_date.month, todays_date.year)

# retreive today's weekday
# M = 0, Tu = 1, W = 2, Th = 3, F = 4, Sat = 5, Sun = 6
print("Today's weekday number: ", todays_date.weekday())

# Datetime Object
today = datetime.now()
print("The current date and time is: ", today)

# Getting the current time
time_now = datetime.time(datetime.now())
print("The current time is ", time_now)

# Date Formatting
# Y will give the 4 digit year
print(today.strftime("The current year is: %Y"))

# a abbreviated day name, d is day of the month, B is the full month name, y is the last two digits of the year
print(today.strftime("%a, %d %B, %y"))

# %c = locale;s date and time, %x locale's date, %X
print(today.strftime("Locale date and time: %c"))
print(today.strftime("Locale date: %x"))
print(today.strftime("Locale date: %X"))

# Time Formatting
# %I/%H = 12/24hour, %M = Minute, %S = seconds, %p Locale's AM/PM
print(today.strftime("Current Time: %I:%M:%S %p"))
print(today.strftime("Current Time: %H:%M"))


# Timedelta
print(timedelta(days=365, hours=5, minutes=1))

# printing today's date one year from now
print("In one year it will be: ", today + timedelta(days=365))

# Using timedelta with more than two parameter
print("In two weeks and 3 days it will be: ",
      today + timedelta(weeks=2, days=3))

# calculating date 1 week ago
print("One week ago today was: ", today - timedelta(weeks=1))
