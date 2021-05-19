# global variable
x = "awesome"


def myfunc():
    print("Python is " + x)


myfunc()


x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)


def myfuncglobal():
    global x
    x = "fantastic"


myfunc()
myfuncglobal()

print("Python is " + x)



