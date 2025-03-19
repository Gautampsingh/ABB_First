
class Player:

    def __init__(self,name, age):
        self.name = name
        self.age = age
        print('Player Ctor......')

    def get_detials(self):
        print(f"Name is {self.name}\nAge is {self.age}")

    @classmethod
    def CreatePlayer(cls, fn, ln, age):
        print("factory....")
        return cls(f"{fn} {ln}", age)      # calls the constructor


ply1 = Player("Virat Kholi", 29)
ply1.get_detials()

print("-" * 60)

ply2 = Player.CreatePlayer("Rohit", "Sharma", 38)
ply2.get_detials()


