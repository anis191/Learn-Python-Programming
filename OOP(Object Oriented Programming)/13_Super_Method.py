class Student:
    University = "Premier University Chittagong"
    def __init__(self, dept, section):
        self.dept = dept
        self.section = section

class greetings:
    def hello(self):
        print(f"Hello {self.Name}")

class info(Student, greetings):
    def __init__(self, name, id, dept, section):
        self.Name = name
        self.Id = id
        super().__init__(dept,section)
        super().hello()

# Input Data:
std1 = info("Ariful Islam",2314,"CSE",'A')

# Show/Output data:
# std1.hello()
print("Your Id: ",std1.Id)
print("Your Department: ",std1.dept)
print("Your Section: ",std1.section)
print("Your University: ",std1.University)