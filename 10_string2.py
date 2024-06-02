a1 = "Hello"
a2 = "World"
print(a1 + a2) #We can concat two string using "+"
num = 10
# print(num + a1) --> It's wrong! We can't concat a string and a number(int,float...)
num = str(num)
print(num + a1) #Here we convert the number into string, than we concat it.
#We can save and print a paragraph or multiple line string, with (''' ''')
p = '''
This is Python
Hello World
'''
print(p)