class Account:
    name = "anonymous"
    def __init__(self, Name):
        self.Name = Name
    
    def __hello(self):  #Now it's a private method
        print(f"Hello, {self.Name}")
    
    def welcome(self):
        self.__hello()
    
user1 = Account("Asik")
print(user1.Name)

try:
    user1.hello()
except Exception as error:
    print("Error:",error)
    print("hello() is private method. It can't access here")

# Now we call private method "hello()", using normal "welcome()" method.
user1.welcome()