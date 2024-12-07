class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass #We can do a attributes private using (__) before it.
    
    def showPass(self):
        print(self.__acc_pass) #It can access any private attributs, because it inside in class.

user1 = Account(1234, "abcd")
print(user1.acc_no)
try:
    print(user1.__acc_pass)
except Exception as error:
    print("__acc_pass is a private attributes")

user1.showPass()