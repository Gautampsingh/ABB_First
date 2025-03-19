"""
def add(x, y):
    return x + y

res = add(10, 20)
print(f"res :{res}")
print('-' * 60)


"""
def outerFun(gname):
    
    def innerFun():

        print("Hello World.....")
        print(f"Greetings {gname}")

    return innerFun

print(f"outerFun.__name__ :{outerFun.__name__}")
print(f"outerFun('rahul').__name__ :{outerFun('rahul').__name__}")

print("-" * 60)

outerFun("Rahul")()             # calls innerFun

print("-" * 60)

inref = outerFun("Sachin")

# after few lines of code
print("Python Traning")
print("Python Traning")
print("Python Traning")
print("Python Traning")
print("Python Traning")

print("-" * 60)

inref()
