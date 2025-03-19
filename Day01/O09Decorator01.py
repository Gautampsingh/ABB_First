
def funLogger(fnc):
    def helper(x, y):
        print("My info logged in a service....")
        fnc(x, y)
        print("My info logged channel closed......")
        print("-" * 60)

    return helper

@funLogger
def add(x, y):
    print('add called....')
    print(x + y)

@funLogger
def sub(x, y):
    print("difference called....")
    print(x - y)

add(120, 380)
sub(800, 532)