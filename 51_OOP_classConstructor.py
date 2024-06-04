# In c++ constractor is --> class_name(parameters){}
# In python constructor is --> (__init__) function
# Syntax -->
'''
class Class_name:
    def __init__(self,fullname):  # "self" is the fixed parameter for a constractor
        self.name = fullname      # Here (name)-> is class variable and (fullname)-> is constractor variable

object_name = class_name(values...)
'''
class Student():
    university = "PUC"  #This data/value is for all object
    def __init__(self,name,id,cg,city):
        self.name = name 
        self.id = id
        self.cg = cg
        self.city = city

stu1 = Student("Anisul Alam",2314,3.22,"ctg")
stu2 = Student("Karim cwo.",3455,4.22,"dhaka")
stu3 = Student("Rahim uddin",5231,4.10,"pabna")
stu4 = Student("Robi",2300,2.22,"kulna")

print(stu1.name, stu1.id, stu1.cg, stu1.city, stu1.university)
print(stu2.name, stu2.id, stu2.cg, stu2.city, stu2.university)
print(stu3.name, stu3.id, stu3.cg, stu3.city, stu3.university)
print(stu4.name, stu4.id, stu4.cg, stu4.city, stu4.university)

# If we need a variable/data which is same for all object. We write it out of the constructor(__init__). Like:- [university="PUC"]. This data is store for object.