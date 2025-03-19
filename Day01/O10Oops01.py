
class Player:           # pascal casing
    # calls the default constructor

    def get_runs(self):
        print("runs scored......")

# creating an object of the class
sachin = Player()

# acess the methods of a class with an object
sachin.get_runs()

print("-" * 60)
print(type(sachin))         # RTTI = Run Time Type Identification

print("-" * 60)
print(sachin.__class__)
