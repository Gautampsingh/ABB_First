
from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def doJob(self):
        pass


class Manager(Employee):

    def doJob(self):
        print("Manager's job......")

class Developer(Employee):

    def doJob(self):
        print("Coding job......")


# polymorphism
def BankFun(emp):
    print("Bank job started.....")
    emp.doJob()
    print("Bank job completed......")
    print("-" * 60)


mike = Manager()
david = Developer()

BankFun(mike)
BankFun(david)
