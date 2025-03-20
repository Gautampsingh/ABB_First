
print("hello world".center(60, "-"))

def fun(a: int, b: int):
    c = a + b
    return c

print(fun(10, 20))
print(fun("hello ", "world"))

print("-" * 60)
print(fun.__annotations__)


