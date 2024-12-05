class Students:
    University = "ABC University" 
    def __init__(self, Name, Id, Age):
        self.Name = Name
        self.ID = Id
        self.Age = Age
    
    @staticmethod      #This keyword create a method to static method.
    def welcome():
        print("Welcome EveryOne!")

std1 = Students("Anisul Alam", 2314, 23)
std2 = Students("Karim", 2214, 24)
std3 = Students("Asif", 3131, 25)

std1.welcome()
print("1st student: ",std1.Name, std1.ID, std1.Age, std1.University)
std2.welcome()
print("2nd student: ",std2.Name, std2.ID, std2.Age, std2.University)
std3.welcome()
print("3rd student: ",std3.Name, std3.ID, std3.Age, std3.University)