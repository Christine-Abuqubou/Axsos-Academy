class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def print_all_information(self):
        print("Name", self.name, "age", self.age, "gender", self.gender)


class Employee(Person):
    employee_count=0
    total_salary=0
    def __init__(self, name, age, gender, salary):
        self.salary = salary
        super().__init__(name, age, gender)
        Employee.employee_count +=1
        Employee.total_salary +=salary
        
      

    def print_all_information(self):
        print(
            "Name",
            self.name,
            "age",
            self.age,
            "gender",
            self.gender,
            "salary",
            self.salary
        )


class Manager(Employee):
    total_target=0
    def __init__(self, name,age,gender,salary,location,id ):
        self.id = id
        self.location = location
        super().__init__(name, age, gender, salary)

    def print_all_information(self):
        print(
            "Name",
            self.name,
            "age",
            self.age,
            "gender",
            self.gender,
            "salary",
            self.salary,
            "location",self.location,
            "id",self.id,
        )
        
        
class Ceo(Manager):
    def __init__(self, name, age, gender, salary,location,id):
       
        super().__init__(name, age, gender, salary,location,id)
        
    
    def print_all_information(self):
        print(
            "Name",
            self.name,
            "age",
            self.age,
            "gender",
            self.gender,
            "salary",
            self.salary,
            "location",self.location,"id",self.id
        )

manager1=Manager("adam",30,"male",2000,"palestine",123)
ceo1=Ceo("adam",30,"male",2000,"palestine",123)
manager1.print_all_information()

emp1=Employee("tim",40,"male",5000)
Employee.print_all_information(emp1)
ceo1=Ceo("habeb",30,"male",20000,"palestion",144)
ceo1.print_all_information()
Manager.print_all_information(ceo1)
Employee.print_all_information(ceo1)


p=Person("alex",28,"female")
for person in [p,emp1,manager1,ceo1]:
    Person.print_all_information(person)

print("Total Employees",Employee.employee_count)
print("Total salary",Employee.total_salary)