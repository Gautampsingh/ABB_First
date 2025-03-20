
import time

class TimeCalculator:

    def __init__(self, fnc):
        self.fnc = fnc

    def __call__(self, *args, **kwargs):
        print("Execution started.....")
        start_time = time.perf_counter()
        result = self.fnc(*args, **kwargs)
        end_time = time.perf_counter()
        print("Execution completed......")
        print(f"Total time taken by function fun to execute :{end_time - start_time} seconds")
        return result


lst = []

@TimeCalculator
def fun(n):
    for i in range(n):
        for j in range(1, i+1):
            lst.append(j ** 3)

print(fun(6500))

