class Car:      #Parent class/base
    color = "Black"

    @staticmethod
    def start():
        print("Car started..")
    
    @staticmethod
    def stop():
        print("Car stopped..")

class Dell_Car(Car):    #Child class/derived
    def __init__(self, Name):
        self.Name = Name

car1 = Dell_Car("Rolls Royce")
print(car1.Name)

try: car1.start() 
except Exception as e: print("Error:",e)

print(car1.color)
car1.stop()