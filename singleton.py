"""

Singleton Design Pattern(creational)

Singleton is a Creational design template that 
ensures that only one instance or object is created
from a class.

for example import madule in python enjoyment from this design pattern

(((learn meta classes)))

"""

class Singletone(type):
    _instance = None

    def __call__(self, *args, **kwds):
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance

class Db(metaclass = Singletone):
    pass

d1 = Db()
d2 = Db()

print(f'{id(d1)}\n{id(d2)}')