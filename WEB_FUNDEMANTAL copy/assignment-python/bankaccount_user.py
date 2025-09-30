class Bank_Account:
    def __init__(self, rate=0.02, balance=0):
        self.rate = rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        

    def withdrow(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("no balance")
        

class User :
        def __init__(self,username,bank_account):
            self.username=username
            self.bank_account=bank_account
            

        def display_balance(self):
            print(f"{self.username} {self.bank_account} ")
            
        
account1=Bank_Account(0.05 ,200)
account2=Bank_Account(0.08,500)
amal=User("amal",600)
christine= User("Christine",account1)

amal.display_balance()
christine.display_balance()
