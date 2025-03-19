
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

ply1 = Player("Sachin", 36)
ply1.get_details()

print("-" * 60)
ply2 = Player("Rahul", 32)
ply2.get_details()

print("-" * 60)
# self will have the name of the object that called the function
ply1.get_details()
print(ply1.__dict__)

print("-" * 60)
ply2.runs = 120
print(ply2.__dict__)

print("-" * 60)
print(ply1.__dict__)




