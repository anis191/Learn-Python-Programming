class Student:
    def __init__ (self, name):
        self.Name = name

s1 = Student("Anis")
print(s1.Name)

s2 = Student("Karim")
print(s2.Name)

# delete object or attributes using "del" keyword:
del s1.Name
print(s1)
try:
    print(s1.Name)
except Exception as error:
    print("Error:",error)

del s2
try:
    print(s2)
    print(s2.Name)
except Exception as error:
    print("Error:",error)