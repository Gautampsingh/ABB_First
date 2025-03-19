
from datetime import date

class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def get_details(self):
        print(f"Name is :{self.name}\nAge is :{self.age}")


    @classmethod
    def CreatePlayer(cls, name, dob):
        age = Player.calcAge(dob)
        return cls(name, age)


    @staticmethod
    def calcAge(dob):
        today = date.today()
        year, month, day = map(int, str(dob).split("-"))
        dob = date(year, month, day)
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return age


ply1 = Player("Rohit", 28)
ply1.get_details()

print("-" * 60)

ply2 = Player.CreatePlayer("Jack", "1989-08-21")
ply2.get_details()
