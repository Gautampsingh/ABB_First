"""
comparison operators - ==, !=, >, >=, <, <=

if we are overloading comparison operators then
1. we have to overload == (mandatory)
2. we have to overload one more comparison operator (with ==)

in this case we can implement a decorator @totalordering for the class so all other comparison operators will work

"""
from functools import total_ordering

@total_ordering
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

# if we overload equal to operator then it automatically overloads not equal to operator
    def __eq__(self, other):
        return self.salary == other.salary

# if we overload greater than operator then it works for less than also
    def __gt__(self, other):
        return self.salary > other.salary


emp1 = Employee('Tim', 6000)
print(emp1)

print("-" * 60)

emp2 = Employee("Kevin", 12000)
print(emp2)

print("-" * 60)

if emp1 < emp2:
    print("{} salary of {} is less than {} salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
else:
    print("{} salary of {} is greater than {} salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))

print("-" * 60)
# compares their addresses by default

if emp1 != emp2:
    print("{} salary of {} is NOT equal to {} salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
else:
    print("{} salary of {} is equal to {} salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))

print("-" * 60)

print(emp1 >= emp2)
