# File open:-
# Syntax --> variable = open ("file_name/file_location","mode")
# mode --> (r:just read) and (w:write)

# File read:- We read a file using read function
# Syntax --> variable = file.read()
f = open("Files for file input output/google.txt","r")
a = f.read()
print(a)
# File close:- When we open a file, after all we need to close this file
# Syntax --> file.close()
f.close()

# Process:-
'''
1st --> Open a file [open()]
2nd --> Read/Write [read()/write("...")]
3rd --> Close the file [close()]
'''