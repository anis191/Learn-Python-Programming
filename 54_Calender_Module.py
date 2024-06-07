# We can create a calender using "calendar" module.
'''
Syntax -->
import calendar
1.For a specific month calender --> calender.month(year_value, month_value)
2.For a specific year calender --> calender.calender(year_value)
'''
# At first we need to import the calendar module
import calendar

# Take month and year as user input
yy = int(input("Enter Year: "))
mm = int(input("Enter Month: "))

# Display calender of a specific month:-
print(calendar.month(yy, mm))

# Display calender of a specific year:-
print(calendar.calendar(yy))