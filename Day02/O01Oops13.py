"""
class
object
call methods in a class
constructor __init__
destructor __del__
self, __dict__
class attribute
class method @classmethod
static method @staticmethod
Operator overloading (magic methods)
__str__(), __eq__(), __gt__(), @total_ordering
__add__(), __sub__(), __mul__(), __truediv__(), __floordiv__()
__iter__(), __len__(), append, __setitem__(), __getitem__()
"""
# private variable

class Employee:

    def __init__(self, name):
        self.__name = name      # private variable
        self.tech = ['C++', 'Java', 'J2EE', 'Spring', 'Hibernate', 'Angular', 'React', 'Python']

    def __str__(self):
        return self.__name + " - " + ", ".join([str(v) for v in self.tech])

emp1 = Employee('Jack')
print(emp1)

print("-" * 60)
# print(emp1.__name)
# print(emp1.__dict__)
emp1._Employee__name = 'Peter'
print(emp1)

print("-" * 60)
print(emp1.__dict__)

