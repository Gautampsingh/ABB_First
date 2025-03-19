
def outerFun(greet):

    def innerFun(sep):

        def innerMostFun(gname):
            from emojis import emojis

            emojized = emojis.encode(greet + " :" + sep + ": " + gname)
            print(emojized)

        return innerMostFun

    return innerFun

KanGrt = outerFun("Namaskara")

TgrKanGrt = KanGrt("tiger")

TgrKanGrt("Prabhakar")


"""
engGrt = outerFun("Hello")
hndGrt = outerFun("Namaskar")

sngArwengGrt = engGrt("----->")
dblArwengGrt = engGrt("=====>>")
sngArwhndGrt = hndGrt("------>")

sngArwengGrt("Sachin")
dblArwengGrt("Rahul")
sngArwhndGrt("Jadeja")

"""