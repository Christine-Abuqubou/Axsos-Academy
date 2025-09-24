class User:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        

    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdrew(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("no balance u cant withdrow ")
        return self

    def display_user_balance(self):
        print(f"{self.name}  {self.balance}")
        # print("User:{} , balance:{}").format(self.name, self.balance)
        return self


christine = User("christine", 300)
amal = User("Amal", 600)
tim = User("Tim", 100)


christine.make_deposit(100).make_deposit(50).make_withdrew(100).display_user_balance()
amal.make_deposit(500).make_withdrew(50).make_withdrew(100).display_user_balance()
tim.make_deposit(100).make_deposit(50).make_withdrew(100).make_withdrew(50).make_withdrew(100).display_user_balance()
