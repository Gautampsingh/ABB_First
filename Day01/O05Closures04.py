# *args and **kwargs

# data is stored in a tuple

def fun(*args):
    print(args)
    print(*args)            # upack
    print("-" * 60)

fun()
fun(1)
fun(1, 2)
fun(1, 2, 3)
fun(1, 2, 3, 4)

print("-" * 60)

def sum(x, y):
    print(f"Adding {x} and {y}")
    return x + y

def diff(x, y):
    print(f"Subtracting {y} from {x}")
    return x - y

# HOF - Higher Order Functions - any function that takes another function as an argument or returns a function as reference
def log_detials(fnc):
    log_info = "logging into a service...."

    def innerFun(*args):
        print(log_info)
        print(fnc(*args))
        print("-" * 60)

    return innerFun

sum_logger = log_detials(sum)
diff_logger = log_detials(diff)

sum_logger(46, 82)
diff_logger(344, 128)
