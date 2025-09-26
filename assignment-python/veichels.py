class Vehicle:
   total_vehicles = 0
   def __init__(self, brand="Unknown", speed=0):
       self.brand = brand
       self.speed = speed
       Vehicle.total_vehicles += 1
   def print_info(self):
       print(f"Vehicle: {self.brand}, Speed: {self.speed} km/h")

class Car(Vehicle):
   total_fuel = 0
   def __init__(self, brand="Unknown", speed=0, fuel=0):
       super().__init__(brand, speed)
       self.fuel = fuel
       Car.total_fuel += fuel
   def print_info(self):
       print(f"Car: {self.brand}, Speed: {self.speed} km/h, Fuel: {self.fuel} L")

class Truck(Vehicle):
   def __init__(self, brand="Unknown", speed=0, capacity=0):
       super().__init__(brand, speed)
       self.capacity = capacity
   def print_info(self):
       print(f"Truck: {self.brand}, Speed: {self.speed} km/h, Capacity: {self.capacity} tons")

class ElectricCar(Car):
   total_battery = 0
   def __init__(self, brand="Unknown", speed=0, fuel=0, battery=0):
       super().__init__(brand, speed, fuel)
       self.battery = battery
       ElectricCar.total_battery += battery
   def print_info(self):
       print(f"ElectricCar: {self.brand}, Speed: {self.speed} km/h, Fuel: {self.fuel} L, Battery: {self.battery} kWh")
   # Explicit parent method calls
   def show_as_car(self):
       print("\n[Forcing Car.print_info]")
       Car.print_info(self)
   def show_as_vehicle(self):
       print("\n[Forcing Vehicle.print_info]")
       Vehicle.print_info(self)
   def show_using_super(self):
       print("\n[Calling immediate parent (Car) via super()]")
       super().print_info()

v1 = Vehicle("Generic", 80)
c1 = Car("Toyota", 120, 50)
t1 = Truck("Volvo", 100, 20)
e1 = ElectricCar("Tesla", 150, 0, 100)
# Polymorphism in action
for v in [v1, c1, t1, e1]:
   v.print_info()
print("\n--- Stats ---")
print("Total Vehicles:", Vehicle.total_vehicles)
print("Total Fuel (Cars):", Car.total_fuel)
print("Total Battery (ElectricCars):", ElectricCar.total_battery)
# Explicit parent calls
e1.show_as_car()
e1.show_as_vehicle()
e1.show_using_super()