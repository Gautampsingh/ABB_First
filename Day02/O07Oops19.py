
class Animal:

    def eat(self):
        print("Animals eat....")

class Bird(Animal):

    def fly(self):
        print("Birds fly.....")

class Chicken(Bird):

    def message(self):
        print("Chickens are breeded for consumption......")

    # override parent class method
    def fly(self):
        print("Chickens seldom fly.....")


chick = Chicken()
chick.eat()
chick.fly()
chick.message()

