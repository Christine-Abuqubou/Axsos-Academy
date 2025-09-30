class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def make_deposit(self, amount):
        self.balance += amount

    def make_withdrew(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("no balance u cant withdrow ")

    def display_user_balance(self):
        print(f"{self.name}  {self.balance}")

christine=User("christine" ,300)
amal=User("Amal",600)
tim=User("Tim" ,100)

christine.display_user_balance()
amal.display_user_balance()
tim.display_user_balance()

christine.make_deposit(100)
christine.make_deposit(50)
christine.make_deposit(50)
christine.make_withdrew(100)
christine.display_user_balance()
amal.make_withdrew(50)
amal.make_withdrew(100)
amal.make_deposit(50)
amal.make_deposit(500)
amal.display_user_balance()

tim.make_withdrew(50)
tim.make_withdrew(100)
tim.make_withdrew(50)
tim.make_deposit(50)
tim.display_user_balance()
