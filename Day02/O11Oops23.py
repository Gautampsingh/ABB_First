# duck types

class  Manager:
    def doJob(self):
        print("Manager's job.......")


class Developer:
    def doJob(self):
        print("Coding job.......")

class Clerk:

    def doJob(self):
        print("Administration job......")


mike = Manager()
dave = Developer()
kevin = Clerk()

def BankFunJobs(emps):
    print("Job started".center(60, "-"))
    for emp in emps:
        emp.doJob()
    print("Job completed".center(60, "-"))
    print("-" * 60)

BankFunJobs([mike, dave, kevin])

