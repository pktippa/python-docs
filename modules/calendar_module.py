import calendar
day = 5
month = 8
year = 2015
# Returns index as 2
dayOfWeekIndex = calendar.weekday(year, month, day)
# Get the day of week from the index
dayOfWeekByName = calendar.day_name[dayOfWeekIndex]
# Prints Wednesday
print(dayOfWeekByName)