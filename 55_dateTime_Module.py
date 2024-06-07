# In python "datetime" module give us current date and time(year,month,day,hour,minute,second,micro-second.
'''
Syntax -->
import datetime
1.For current date and time(according to my device)--> datetime.datetime.now()
2.Create a custom date--> datetime.datetime(year,month,day)
'''
# At first we need to import the datetime module
import datetime

# For current date and time(according to my device):-
x = datetime.datetime.now()
print(x)

# Create a custom date:-
y = datetime.datetime(1971,7,21)
print(y)