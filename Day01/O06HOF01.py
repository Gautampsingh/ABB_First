
def callMe():
    print(f"Apple Ooty")


def fun(fnc):
    print("Hello")
    fnc()
    print("hi")
    print('_' * 40)

    def defineMe():
        print(f"Orange Kanpur")

    return defineMe


def funCallback(fnc):
    print("Mera Barath Mahan...")
    fnc()
    print("India is Great...")


funCallback(fun(callMe))
