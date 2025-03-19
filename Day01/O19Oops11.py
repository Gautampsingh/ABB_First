
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name   :{self.name}\nSalary  :{self.salary}"

    # arithmetic Operators

    def __add__(self, other):
        return Employee("noName", self.salary + other.salary)

    def __sub__(self, other):
        return Employee("noName", self.salary - other.salary)

    def __mul__(self, other):
        return Employee("noName", self.salary * other.salary)

    def __truediv__(self, other):
        return Employee("noName", self.salary / other.salary)

    def __floordiv__(self, other):
        return Employee("noName", self.salary // other.salary)

emp1 = Employee("Jack", 150)
print(emp1)

print("-" * 60)
emp2 = Employee("Tina", 200)
print(emp2)

print("-" * 60)
emp3= Employee("Corey", 385)
print(emp3)

print("-" * 60)
# add
print(emp1 + emp2 + emp3)

print("-" * 60)
# sub
print(emp3 - emp2 - emp1)

print("-" * 60)
# mul
print(emp1 * emp2 * emp3)

print("-" * 60)
# div
print(emp1 / emp2 / emp3)

print("-" * 60)
# floor div
print(emp1 // emp2 // emp3)