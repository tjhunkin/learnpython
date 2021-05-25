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

# unlimited arguments


def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")

# named arguments


def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="Emil", child2="Tobias", child3="Linus")

# unlimited named parameters


def my_function(**kid):     # **kwargs
    print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Refsnes")

# default parameter value


def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# return values


def my_function(g):
    return 5 * g


print(my_function(3))
print(my_function(5))
print(my_function(9))

# recursion


def tri_recursion(k):

    print("k:" + str(k))

    if k > 0:
        output = tri_recursion(k - 1)
        print("output:" + str(output))
        result = k + output
        print("result:" + str(result))
    else:
        result = 0
        print("result:" + str(result))
    return result


print("\n\nRecursion Example Results")
tri_recursion(2)


# scope for nested functions
def myfunc():
    x = 300     # The local variable can be accessed from a function within the function:

    def myinnerfunc():
        print(x)

    myinnerfunc()


myfunc()
