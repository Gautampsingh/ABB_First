
class Animal:

    def __init__(self):
        print("Animal Ctor......")
        self.age = '1 year'

    def eat(self):
        print("Animals eat....")

# inheritance
class Bird(Animal):

    def fly(self):
        print("Birds fly.....")

class Fish(Animal):

    def swim(self):
        print("Fishes swim.....")

cuckoo = Bird()
cuckoo.eat()
cuckoo.fly()

print("-" * 60)

dolphin = Fish()
dolphin.eat()
dolphin.swim()

print("-" * 60)
print(f"cuckoo  :{cuckoo.__dict__}")
print(f"dolphin :{dolphin.__dict__}")

print("-" * 60)
print(f"isinstance(cuckoo, Bird) :{isinstance(cuckoo, Bird)}")
print(f"isinstance(cuckoo, Fish) :{isinstance(cuckoo, Fish)}")
print(f"isinstance(cuckoo, Animal) :{isinstance(cuckoo, Animal)}")
print(f"isinstance(cuckoo, object) :{isinstance(cuckoo, object)}")

print("-" * 60)
print(f"isinstance(dolphin, Bird) :{isinstance(dolphin, Bird)}")
print(f"isinstance(dolphin, Fish) :{isinstance(dolphin, Fish)}")
print(f"isinstance(dolphin, Animal) :{isinstance(dolphin, Animal)}")
print(f"isinstance(dolphin, object) :{isinstance(dolphin, object)}")

print("-" * 60)
print(f"issubclass(Bird, Animal) :{issubclass(Bird, Animal)}")
print(f"issubclass(Bird, object) :{issubclass(Bird, object)}")
print(f"issubclass(Bird, Fish) :{issubclass(Bird, Fish)}")

