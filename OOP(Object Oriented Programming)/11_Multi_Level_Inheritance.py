class Car:
    color = "Black"
    @staticmethod
    def info():
        print("Manufactured by: Toyota")
        print("VIN No: 2145999CF")
        print("License Date: 22/03/2023")

class Specifications(Car):
    @staticmethod
    def Engine():
        print("Type: Petrol, Diesel")
        print("Drivetrain: FWD,RWD,AWD")
    Capacity = '1500cc.'

class Dell_car(Specifications):
    def __init__(self, name):
        self.Name = name

car1 = Dell_car("BMW")
print(car1.Name)

try :car1.Engine()
except Exception as e : print(e)
print(car1.Capacity)

try: car1.info()
except Exception as e: print(e)

print(car1.color)