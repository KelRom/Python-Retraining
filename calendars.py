import calendar

# creating a plain text calendar
text_calendar_obj = calendar.TextCalendar(calendar.SUNDAY)

thestr = text_calendar_obj.formatmonth(2026, 1, 0, 0)
print(thestr)

# Creating an html calendar
html_calendar = calendar.HTMLCalendar(calendar.SUNDAY)
thestr = html_calendar.formatmonth(2026, 1)
print(thestr)

# loop over the days of the month
for i in text_calendar_obj.itermonthdays(2026, 8):
    print(i)

for name in calendar.month_name:
    print(name)

print()
for day in calendar.day_name:
    print(day)

# calculating days based on a rule
print()
print("Team meetings will be on:")
for m in range(1, 13):
    cal = calendar.monthcalendar(2026, m)
    weekone = cal[0]
    weektwo = cal[1]
    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]

    print(f"{calendar.month_name[m]}: {meetday}")
