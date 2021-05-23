# lambda arguments : expression

x = lambda a: a + 10
print(x(5))

# multiple arguments

x = lambda a, b: a * b
print(x(5, 6))


# usage


def myfunc(n):
    return lambda a: a * n


# set value for n
mydoubler = myfunc(2)

# set value for a
print(mydoubler(11))


mytripler = myfunc(3)

print(mytripler(11))
