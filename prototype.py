"""
prototype design pattern

This design template provides a way to create a new object 
by copying it from other existing objects.Using this technique,
new objects can be created in the software without creating a 
connection between the new object and the class from wich it is made.

"""

from copy import deepcopy

class Person:
    def __init__(self , name , age):
        self.name = name
        self.age = age

class prototype:
    def __init__(self):
        self._object = {}

    def register(self , name , obj):
        self._object[name] = obj
    
    def unregister(self , name):
        del self._object[name]


    def clone(self , name , **kwargs):
        cloneObj = deepcopy(self._object.get(name))
        cloneObj.__dict__.update(kwargs)
        return cloneObj


p1 = Person("amir" , "24")

pro1 = prototype()
pro1.register('person1' , p1)

personcopy = pro1.clone('person1' , age = '25')

print(personcopy.__dict__)
print(p1.age)