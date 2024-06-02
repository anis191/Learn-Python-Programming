'''
in :- (in) keyword also work like find() function.It will check a character/word/substring
in a string. If it found, it was return "True" and return "False" if not found.
'''
# Syntax --> x = 'character' in string
name = "Tony Stark"
x = 'y' in name
print(x)
x = 'z' in name
print(x)

# Syntax --> x = "word/ksubstring" in string
line = "Hey, How are you?"
x = "How" in line
print(x)
x = "Are" in line
print(x)