"""
This design pattern is for making objects like a hierarchial 
tree when it is supposed to a group of objects used to behave 
similarly
in this example I am modeling this design pattern
"""

from abc import ABC , abstractmethod

class World(ABC):
    @abstractmethod
    def show(self):
        pass

class Being(World):
    def __init__(self,name):
        self.name = name
        self.children = []

    def add(self,object):
        self.children.append(object)

    def remove(self , object):
        self.children.remove(object)

    def show(self):
        print(f'Bieng Composite {self.name}')
        for child in self.children:
            child.show()


class Animal(World):
    def __init__(self , name):
        self.name = name
        self.children =[]
    
    def add(self,object):
        self.children.append(object)

    def remove(self , object):
        self.children.remove(object)

    def show(self):
        print(f'\tAnimal Composite {self.name}')
        for child in self.children:
            child.show()

class Human(World):
    def __init__(self , name):
        self.name = name
        self.children =[]
    
    def add(self,object):
        self.children.append(object)

    def remove(self , object):
        self.children.remove(object)

    def show(self):
        print(f'\tHuman Composite {self.name}')
        for child in self.children:
            child.show()

class Cat(World):
    def __init__(self , name):
        self.name = name

    def show(self):
        print(f"\t\tcat leaf {self.name}")

class Dog(World):
    def __init__(self , name):
        self.name = name

    def show(self):
        print(f"\t\tdog leaf {self.name}")

class Male(World):
    def __init__(self , name):
        self.name = name

    def show(self):
        print(f"\t\tmale leaf {self.name}")

class Female(World):
    def __init__(self , name):
        self.name = name

    def show(self):
        print(f"\t\tfemale leaf {self.name}")



cat = Cat('maloos')
dog = Dog('huski')

male = Male('amir')
female = Female('zahra')

animal = Animal('animal')
human = Human('human')

animal.add(cat)
animal.add(dog)

human.add(male)
human.add(female)

being = Being('being')

being.add(animal)
being.add(human)

being.show()
