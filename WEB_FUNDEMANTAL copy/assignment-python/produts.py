class Product:

    total_products = 0

    total_revenue = 0

    def __init__(self, name="Unknown", price=0, quantity=1):

        self.name = name

        self.price = price

        self.quantity = quantity

        Product.total_products += 1

    def sell(self, qty):

        if qty <= self.quantity:

            cost = qty * self.price

            self.quantity -= qty

            Product.total_revenue += cost

            print(f"Sold {qty} x {self.name} for {cost}")

        else:

            print(f"Not enough {self.name} in stock!")

    def print_info(self):

        print(f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}")


class Electronics(Product):

    def __init__(self, name="Unknown", price=0, quantity=1, warranty_years=1):

        super().__init__(name, price, quantity)

        self.warranty_years = warranty_years

    def warranty_cost(self):

        return self.price * 0.1 * self.warranty_years

    def print_info(self):

        print(f"Electronics: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Warranty: {self.warranty_years} yrs")


class Clothing(Product):

    def __init__(self, name="Unknown", price=0, quantity=1, discount=0.1):

        super().__init__(name, price, quantity)

        self.discount = discount

    def discounted_price(self):

        return self.price * (1 - self.discount)

    def sell(self, qty):

        if qty <= self.quantity:

            cost = qty * self.discounted_price()

            self.quantity -= qty

            Product.total_revenue += cost

            print(f"Sold {qty} x {self.name} (discounted) for {cost}")

        else:

            print(f"Not enough {self.name} in stock!")

    def print_info(self):

        print(f"Clothing: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Discount: {self.discount*100}%")


class Food(Product):

    def __init__(self, name="Unknown", price=0, quantity=1, days_to_expiry=10):

        super().__init__(name, price, quantity)

        self.days_to_expiry = days_to_expiry

    def is_expired(self):

        return self.days_to_expiry <= 0

    def sell(self, qty):

        if self.is_expired():

            print(f"Cannot sell {self.name}, it has expired!")

        elif qty <= self.quantity:

            cost = qty * self.price

            self.quantity -= qty

            Product.total_revenue += cost

            print(f"Sold {qty} x {self.name} for {cost}")

        else:

            print(f"Not enough {self.name} in stock!")

    def print_info(self):

        status = "Expired" if self.is_expired() else f"{self.days_to_expiry} days left"

        print(f"Food: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Expiry: {status}")

# Create products

laptop = Electronics("Laptop", 1000, 5, warranty_years=2)

shirt = Clothing("T-Shirt", 50, 10, discount=0.2)

bread = Food("Bread", 2, 20, days_to_expiry=0)

# Sell items

laptop.sell(2)

shirt.sell(3)

bread.sell(5)

# Show product info

for item in [laptop, shirt, bread]:

    item.print_info()

print("\n--- Store Stats ---")

print("Total Products:", Product.total_products)

print("Total Revenue:", Product.total_revenue)

print("Laptop Warranty Cost:", laptop.warranty_cost())

print("Shirt Discounted Price:", shirt.discounted_price())
 