
class Player:

    def __init__(self):             # dunder init method - double underscore
        self.name = 'Sachin'
        self.age = 34
        print("Player Initialized......")

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

    # destructor
    def __del__(self):
        print("Object detroyed......")


ply1 = Player()
ply1.get_details()

print("-" * 60)
ply2 = Player()
ply2.name = "Rahul"
ply2.age = 32
ply2.get_details()

print("-" * 60)
print(ply1.__dict__)            # dunder dict

print("-" * 60)

del ply1

print("-" * 60)
