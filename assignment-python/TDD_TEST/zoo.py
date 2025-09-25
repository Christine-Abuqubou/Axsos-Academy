

class Animal:
    def __init__(self, name, age, happiness_level, health):
        self.name = name
        self.age = age
        self.happiness_level = happiness_level
        self.health = health


class Lion(Animal):
    def __init__(self, name, age, happiness_level, health, weight):
        self.weight = weight

        super().__init__( name, age, happiness_level, health)

    def display_info(self):
        print(
            f"{self.name} {self.age} {self.happiness_level} {self.health} {self.weight}"
        )
    def feed(self):
        self.health +=5
        self.happiness_level +=10


class Tiger(Animal):
    def __init__(self, name, age, happiness_level, health, weight):
        self.weight = weight

        super().__init__( name, age, happiness_level, health)

    def display_info(self):
        print(
            f"{self.name} {self.age} {self.happiness_level} {self.health}{self.weight}"
        )
    
    def feed(self):
        self.health +=50
        self.happiness_level +=15



class Cat(Animal):
    def __init__(self, name, age, happiness_level, health, weight):
        self.weight = weight

        super().__init__( name, age, happiness_level, health)

    def display_info(self):
        print(
            f"{self.name} {self.age} {self.happiness_level} {self.health}{self.weight}"
        )
    
    def feed(self):
        self.health +=20
        self.happiness_level +=30

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    # def add_lion(self, name, age, happiness_level, health, weight):
        # self.animals.append(Lion(name,age, happiness_level, health, weight))
    def add_lion(self, lion):
        self.animals.append(lion)

    def add_tiger(self,Tiger):
        self.animals.append(Tiger)
    
    def add_cat(self, Cat):
        self.animals.append(Cat)


    def print_all_info(self):
        print("-" * 30, self.name, "-" * 30)
        for animal in self.animals:
            animal.display_info()




zoo1 = Zoo("John's Zoo")
lion1 = Lion("Nala",5,0,100,80)
lion1.feed()
zoo1.add_lion(lion1)
lion2 = Lion("Simba",5,10,100,50)
lion2.feed()
zoo1.add_lion(lion2)


tiger1 = Tiger("Rajah",50,3,10,0)
tiger1.feed()
zoo1.add_tiger(tiger1)
tiger2=Tiger("Shere Khan",50,40,10,80)
tiger2.feed()
zoo1.add_tiger(tiger2)


cat1=Cat("SHERAZ",10,20,30,40)
cat1.feed()
zoo1.add_cat(cat1)
zoo1.print_all_info()
