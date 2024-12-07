class Person:
    Name = "anonymous"

    @classmethod
    def changeName(cls, new_name):
        cls.Name = new_name

print(Person.Name)

obj = Person()
obj.changeName("Asif")

print(Person.Name)