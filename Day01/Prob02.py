import time

def time_it(fnc):
    def wrapper(arg):
        start_time = time.perf_counter()
        print("Executing the function......")
        fnc(arg)
        print("Completed Executing......")
        end_time = time.perf_counter()
        print(f"Execution time for {fnc.__name__}: {end_time - start_time:.6f} seconds")

    return wrapper


lst = []

@time_it
def fun(n):
    for i in range(n):
        for j in range(1, i + 1):
            lst.append(j ** 3)

fun(6500)