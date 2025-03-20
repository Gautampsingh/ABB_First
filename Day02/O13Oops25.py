
class LessBalance(Exception):
    def __init__(self):
        print("Balance cannot be less than 1000")


act_balance = 500

try:

    if act_balance < 1000:
        raise(LessBalance)          # calls the constructor...

except LessBalance as l:
    print(l)
