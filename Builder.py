
"""
Builder Design Pattern

Usually a designer in the design path starts with the factory method pattern, then
adapts to the abstract factory pattern , the prototype pattern, or the builder pattern
we usully resort to the constructive pattern when we need more flexibility in the design process.

"""
class Director:
    __builder = None

    def setBuilder(self,builder):
        self.__builder = builder
    
    def getCar(self):
        car = Car()

        body = self.__builder.getBody()
        car.setbody(body)

        wheel = self.__builder.getWheel()
        car.setwheel(wheel)

        engine = self.__builder.getEngine()
        car.setengine(engine)

        return car


class Car:
    def __init__(self):
        self.__wheel = None
        self.__engine = None
        self.__body = None

    def setwheel(self , wheel):
        self.__wheel = wheel

    def setengine(self,engine):
        self.__engine = engine

    def setbody(self , body):
        self.__body = body

    def detail(self):
        print(f'Wheel : {self.__wheel.size} Body : {self.__body.shape} Engine : {self.__engine.hp}')


class Builder:
    def getEngine(self):pass
    def getWheel(self):pass
    def getBody(self):pass

class Bmw(Builder):
    def getBody(self):
        body = Body()
        body.shape = 'suv'
        return body

    def getWheel(self):
        wheel = Wheel()
        wheel.size = '22'
        return wheel
    
    def getEngine(self):
        engine = Engine()
        engine.hp = 500
        return engine

class Benz(Builder):
    def getBody(self):
        body = Body()
        body.shape = 'sadan'
        return body

    def getWheel(self):
        wheel = Wheel()
        wheel.size = '18'
        return wheel
    
    def getEngine(self):
        engine = Engine()
        engine.hp = 340
        return engine





class Wheel: size = None
class Body: shape = None
class Engine: hp = None

car1 = Bmw
director = Director()
director.setBuilder(car1())

b1 = director.getCar()
b1.detail()