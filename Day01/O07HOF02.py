
def bank_flow(fnc):         # HOF
    print("-" * 60)
    print("logging in......")
    fnc()
    print("logging out......")
    print("-" * 60)

def withDraw():
    print("Debitted.....")

def deposit():
    print("Credited......")

def gift():
    print("Transfer.......")


bank_flow(deposit)
bank_flow(withDraw)
bank_flow(gift)
