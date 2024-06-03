# add():Adds an element to the set
# Syntax --> set_name.add(item)
num = {1,2,3,4}
num.add(5)
print(num)

num2 = set()
print(num2)
num2.add(15)
print(num2)

name = {"anis","karim"}
print(name)
name.add("robi")
print(name)

#remove(): Removes the specified element
a = {1,2,3,"abc",3.45,False}
print(a)
a.remove(2)
print(a)
a.remove(False)
a.remove("abc")
print(a)

#pop(): Removes an random element from the set
b = {1,2,3,"abc",3.45,False}
b.pop()
print(b)
b.pop()
print(b)