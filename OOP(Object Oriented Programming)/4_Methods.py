class Students:
    University = "ABC University"   #This is called "Class attributes, this data is common data for all object"
    def __init__(self, Name, Id, Age):
        self.Name = Name
        self.ID = Id
        self.Age = Age

    def hello(self):    #This types function inside a class is called "Method"
        print(f"Hello {self.Name}! Welcome")

std1 = Students("Anisul Alam", 2314, 23)
std2 = Students("Karim", 2214, 24)
std3 = Students("Asif", 3131, 25)

std1.hello()
print("1st student: ",std1.Name, std1.ID, std1.Age, std1.University)
std2.hello()
print("2nd student: ",std2.Name, std2.ID, std2.Age, std2.University)
std3.hello()
print("3rd student: ",std3.Name, std3.ID, std3.Age, std3.University)
