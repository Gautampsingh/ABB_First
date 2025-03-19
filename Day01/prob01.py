
def add(a, b):
    return a + b

def fun(x):
    print(f"x :{x}")


fun(100)

print("-" * 60)

fun(40 + 60)

print("-" * 60)

fun(add(40, 60))
