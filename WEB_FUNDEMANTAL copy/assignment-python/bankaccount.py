class Bank_Account:
    def __init__(self, rate=0.02, balance=0):
        self.rate = rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrow(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("no balance")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.rate

    def display_balance(self):
        print(f"{self.balance} {self.rate} ")
        return self


account1=Bank_Account(rate=0.05,balance=100)
account2=Bank_Account(0.08,600)

account1.deposit(100).deposit(50).withdrow(100).display_balance().yield_interest()
account2.deposit(500).withdrow(50).withdrow (100).deposit(50).display_balance().yield_interest()
account1.display_balance()
account2.display_balance()
