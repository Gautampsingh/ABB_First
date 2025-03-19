
def funLogger(fnc):

    def wrapper():
        print("Logged into a service.....")
        fnc()           # call back
        print("Logger channel closed......")
        print("-" * 60)

    return wrapper

def normalFun():
    print("I should be called normal.....")


funLogger(normalFun)    # no output

print("*" * 60)

funLogger(normalFun)()      # calls the wrapper

print("*" * 60)

res_fun = funLogger(normalFun)
res_fun()

print("*" * 60)
normalFun = funLogger(normalFun)
normalFun()               # calls the wrapper

print("*" * 60)

@funLogger              # same as basicFun = funLogger(basicFun)
def basicFun():
    print("I should be called BASIC......")

basicFun()          # calls the wrapper