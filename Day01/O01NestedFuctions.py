
def outerFun():
    gname = "Sachin"                # Local Variable

    def innerFun():

        nonlocal gname    # only local var can be converted as nonlocal
        gname = gname + " Tendulkar"
        print("Hello World.....")
        print(f"Greetings Mr.{gname}")

    innerFun()
    print(f"OuterFun :{gname}")

outerFun()