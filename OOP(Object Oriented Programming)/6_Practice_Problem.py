'''
Create Account class with 2 attributes - balance & account no.
Create methods for debit, credit & printing the balance
'''
class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no
    
    def debit(self, amount):
        self.balance -= amount
        print(f"{amount} tk debit")
        self.current_balance()
    
    def credit(self, amount):
        self.balance += amount
        print(f"{amount} tk credit")
        self.current_balance()
    
    def current_balance(self):
        print(f"Current Balance: {self.balance}")

user1 = Account(5000, 12345)
user2 = Account(10000, 54321)

# See current balance 
user1.current_balance()
user2.current_balance()

# After debit
user1.debit(2000)
user2.debit(5000)

# After Credit
user1.credit(99)
user2.credit(88)