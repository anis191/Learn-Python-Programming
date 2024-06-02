#count(): Returns the number of times a specified value/item occurs in a tuple
num = (1,2,1,3,4,1,3,1,6,8,1,2,3,1)
x = num.count(1)
x2 = num.count(3)
print(x)
print(x2)

name = ("anis","muhi","shariar","anis","Karim")
x3 = name.count("anis")
print(x3)

#index(): Searches the tuple for a specified value and returns the position of where it was found
num2 = (1,2,1,3,4,1,3,1,6,8,1,2,3,1)
x = num2.index(3)
x2 = num2.index(1)
print(x)
print(x2)

name2 = ("anis","muhi","shariar","anis","Karim")
x3 = name2.index("anis")
print(x3)