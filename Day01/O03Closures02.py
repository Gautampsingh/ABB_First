def outerFun(greet):
    # simple curry...
    def innerFun(gname):
        print("Hello World....")
        print(greet, gname)

    return innerFun


engGrt = outerFun("Hello")
hndGrt = outerFun("Namaskar")

engGrt("Sachin...")
print("-" * 60)
hndGrt("Jadeja")
