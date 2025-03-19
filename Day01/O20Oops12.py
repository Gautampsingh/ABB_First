
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tech = ['C++', 'JAVA', 'J2EE', 'Spring', 'Hibernate', 'Angular', 'React']

    def __iter__(self):
        # return self.tech.__iter__()
        return iter(self.tech)

    def append(self, val):
        self.tech.append(val)

    def __len__(self):
        return len(self.tech)

    def __getitem__(self, index):
        return self.tech[index]

    def __setitem__(self, index, value):
        self.tech[index] = value


emp = Employee("Marshal", 35000)
print("-" * 60)

# list Comprehension
print([em for em in emp])

print("-" * 60)

emp.append("Python")
print([em for em in emp])

print("-" * 60)
print(len(emp))

print("-" * 60)
x = emp[4]
print(f"x :{x}")

print("-" * 60)
emp[4] = "Ext JS"
print([em for em in emp])

