# Two read() method:-

#1.Read file as character:[Syntax --> file.read(parameter)]
file = open("Files for file input output/google.txt","r")
a = file.read(5)  #It read only first 5 characters
print(a)
file.close()

#2.Read file data line by line, using readline(). It read only 1 line at a time.
file = open("Files for file input output/google.txt","r")
a = file.readline()
print(a)

for i in range(3):
    print(file.readline())

file.close()