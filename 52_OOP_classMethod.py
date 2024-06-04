#Class Method is nothing but a function, which is written under a class for every/any object
# Syntax -->
'''
def function_name(self):
    //code
call it-->
object.function()
'''
class Student():
    university = "PUC"  #This data/value is for all object
    def __init__(self,name,id,cg,city):
        self.name = name 
        self.id = id
        self.cg = cg
        self.city = city
    
    def welcome(self):
        print("Welcome ", self.name) #This "self" indicate those object, which object use for call this function/method

    def abc(self):
        return self.city

s1 = Student("Anisul Alam",2314,3.22,"ctg")
s2 = Student("Rahim Chow.",2345,4.92,"dhaka")
s1.welcome()
print(s1.name, s1.id, s1.cg, s1.university)
print("City is: ",s1.abc())

s2.welcome()
print(s2.name, s2.id, s2.cg, s2.university)
print("City is: ",s2.abc())