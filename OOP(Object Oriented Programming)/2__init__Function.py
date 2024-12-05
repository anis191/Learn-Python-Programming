'''
__init__ function is nothing but a class constractor.
Syntax -->
Class Class_name:
    def __init__(self, parameters):
        #code
'''

class Students:
    def __init__(self, Name, Id, Age):
        self.Name = Name
        self.ID = Id
        self.Age = Age

# 1st object/ 1st student data:
std1 = Students("Anisul Alam", 2314, 23)

# 2nd object/ 2nd student data:
std2 = Students("Karim", 2214, 24)

# 3ed object/ 3rd student data:
std3 = Students("Asif", 3131, 25)

print("1st student: ",std1.Name, std1.ID, std1.Age)
print("2nd student: ",std2.Name, std2.ID, std2.Age)
print("3rd student: ",std3.Name, std3.ID, std3.Age)
