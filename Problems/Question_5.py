# Python program to swap two variable

#Using 3rd variable
x = 10
y = 5
temp = x
x = y
y = temp
print("x is: ",x)
print("y is: ",y)

#Without 3rd variable
# Syntax --> 1st, 2nd = 2nd, 1st
a = 15
b = 33
a, b = b, a
print("a is: ",a)
print("b is: ",b)