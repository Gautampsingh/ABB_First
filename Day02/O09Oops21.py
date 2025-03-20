
"""
When you want to define a common structure and behaviour for a group of related classes
You want to enforce certain functionalities through abstract methods leaving specific implementation to subclasses

"""

# RBI is framing a rule that all account holders in a bank should get a privilege of checking their bank balance
# abc - module, ABC - class

from abc import ABC, abstractmethod

class Account(ABC):

    def withdraw(self):
        pass

    @abstractmethod
    def checkBalance(self):
        pass


class Savings(Account):

    def withdraw(self):
        print("Debited from the account....")

    def checkBalance(self):
        print("Balance in the account is  ######.##")

sav1 = Savings()
sav1.withdraw()
sav1.checkBalance()

