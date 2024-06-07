'''
strftime()--> return a specific part/value of date time
Syntax --> x = variable.strftime("format_Spacifier")
format_Spacifier:-
1. %b --> Month name in short form(Dec).
2. %B --> Month name in full form(December).
3. %m --> Month as a number 01-12 (12).
4. %y --> Year in short form(18)
5. %Y --> Year in full form(2018)
6. %H --> Hour in 24-hour time format(17)
7. %I --> Hour in 12-hour time format(05)
8. %p --> AM/PM (PM)
9. %M --> Minute 00-59 (41)
'''

import datetime
x = datetime.datetime.now()
print(x)

# %b --> Month name in short form(Dec):-
print(x.strftime("%b"))
# %B --> Month name in full form(December):-
print(x.strftime("%B"))
# %m --> Month as a number 01-12 (12):-
print(x.strftime("%m"))
# %y --> Year in short form(18):-
print(x.strftime("%y"))
# %Y --> Year in full form(2018):-
print(x.strftime("%Y"))
# %H --> Hour in 24-hour time format(17):-
print(x.strftime("%H"))
# %I --> Hour in 12-hour time format(05):-
print(x.strftime("%I"))
# %p --> AM/PM (PM)
print(x.strftime("%p"))
# %M --> Minute 00-59 (41)
print(x.strftime("%M"))