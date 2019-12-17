"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

# print('Calendar of March 2019')
# print(calendar.month(2019,3,2,1))

# print('Calendar for 2020')
# print(calendar.calendar(2020,2,2,6,3))

# print(datetime.today().month)
# print(datetime.today().year)

dt_month = datetime.today().month
dt_year = datetime.today().year

def print_cal(month = dt_month, year = dt_year):
    if 0 < month < 13:
        print(calendar.month(year, month, 2, 1))
    else:
        print("Input must include a month (1-12) or a month and year (month, year) combination")
    

print_cal() #Should print december of 2019 (or current month and year)
print_cal(2) #Should print february of 2019
print_cal(2, 2020) #Should print february of 2020
print_cal(2013, 5) #should throw error