class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @property
    def Age(self):
        return self.age
    
    @Age.setter
    def Age(self, value):
        if(value <= 0):
            print("Age can't negative")
        else:
            self.age = value
    
anis = Person("anis", 23)
print(anis.Age)
anis.Age = 25
print(anis.Age)
anis.Age = 0
print(anis.Age)