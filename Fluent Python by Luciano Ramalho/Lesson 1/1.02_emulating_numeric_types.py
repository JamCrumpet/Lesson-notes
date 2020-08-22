# several special methods allow user objects to respond to operator such as +
# here we will futher illustrate the use of special methods
# here we will implement a class to represent two dimension vectors


# in console:
# >>> v1 = Vector(2,4)
# >>> v2 = Vector(2,1)
# >>> v1+v2
# Vector(4,5)
# note the + operator produces a Vector result


# abs is a build in function that returns the absolute value of integers and floats, and the magnitude of the ...
# ... complex numbers so to be consistent our API also uses abs to calculate the magnitude of a vector:
# v = Vector(3,4)
# >>> abs(v)
# 15.0

# can also implement the * operator to perform scalar multiplication
# >>> v*3
# Vector(9,12)
# abs(v*3)
# 15.0

# the following is a Vector class implement the operations just described though the use of special methods

from math import hypot

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vector(%r ,%r)" % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x,self.y)

    def __bool(self):
        return bool(abs(self))

    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)

    def __mul__(self,scalar):
        return Vector(self.x * scalar, self.y * scalar)

# although four special methods (not including __init__) none of them is directly called with the class or ...
# ... the typical usage of the class illustrated by the console listing


# here we will talk about the special methods used

# __ repr__ is called by the repr build in to get the string representation of the object for inspection ...
# ... if __repr__ was not implemented vector instances would be representing like <Vector obejct at 0x01eXXXXX>
# 