"""
just as objects of python standard data types are picklable, similarly of custom class can also be pickled and unpickled
"""

from pickle import *

class Person:

    def __init__(self):
        self.name = "Rahul"
        self.age = 32

    def show(self):
        print("Name :", self.name, "Age :", self.age)

p1 = Person()
f = open("mypickled.txt", "wb")
dump(p1, f)
f.close()

print("Unpickled Data".center(60, "-"))
f = open("mypickled.txt", "rb")
p1 = load(f)
p1.show()
