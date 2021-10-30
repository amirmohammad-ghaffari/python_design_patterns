'''
Factory method design pattern there with abstract method

'''
"""
example description

Car => Benz , Bmw =>Suv , Coupe
benz suv =>gla
bmw suv =>x1

benz coupe=>cls
bmw coupe=>m2

"""

from abc import ABC, abstractclassmethod

class Car(ABC):
    @abstractclassmethod
    def call_suv(self):
        pass

    @abstractclassmethod
    def call_coupe(self):
        pass
#-----------------------------------------------

class Benz(Car):

    @staticmethod
    def call_suv(model):
        return(model)

    @staticmethod
    def call_coupe(model):
        return(model)

class Bmw(Car):
    @staticmethod
    def call_suv(model):
        return(model)
    
    @staticmethod
    def call_coupe(model):
        return(model)

#-----------------------------------------------

class Suv(ABC):
    @abstractclassmethod
    def creating_suv(self):
        pass

class Coupe(ABC):
    @abstractclassmethod
    def creating_coupe(self):
        pass

#-----------------------------------------------

class Gla(Suv):
    def creating_suv(self):
        print("This is your Suv Benz Gla...")

class Gla1(Suv):
    def creating_suv(self):
        print("This is your Suv Benz Gla1...")


class X1(Suv):
    def creating_suv(self):
        print("This is your Suv Bmw X1...")

class X2(Suv):
    def creating_suv(self):
        print("This is your Suv Bmw X2...")

class Cls(Coupe):
    def creating_coupe(self):
        print("This is your Coupe Benz Cls")

class Cls1(Coupe):
    def creating_coupe(self):
        print("This is your Coupe Benz Cls1...")

class M1(Coupe):
    def creating_coupe(self):
        print("This is your Coupe Bmw M1...")

class M2(Coupe):
    def creating_coupe(self):
        print("This is your Coupe Bmw M2...")

class M3(Coupe):
    def creating_coupe(self):
        print("This is your Coupe Bmw M3...")

#-----------------------------------------------

def clientSuv(carf , model):
    suv = carf.call_suv(model())
    suv.creating_suv()

def clientCoupe(carf , model) :
    coupe = carf.call_coupe(model())
    coupe.creating_coupe()


clientCoupe(Bmw , M2)
clientCoupe(Benz , Cls)
clientCoupe(Bmw , M3)

 