# find() : Searches the string for a specified value and returns the position of where it was found
# 1. Find a character:-
# Syntax --> x = string.find('character')
name = "Tony stark" #find 's'
x = name.find('s') #When found, it will return it's index no
print(x)
x = name.find('S')  #If not found, it will return (-1)
print(x)

# 2. Find a word:-
# Syntax --> x = string.find('word')
name2 = "Hey, I am robi"
x = name2.find('robi') #When found, it will return it's 1st character index no.
print(x)
x = name2.find('Robi')
print(x)   #If not found, it will return (-1)

# Find a substring:-
# Syntax --> x = string.find('substring')
print(name2.find("I am robi")) #When found, it will return it's 1st character index no.
#If not found, it will return (-1)