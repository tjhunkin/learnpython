import mymodule  # mymodule.py
import mymodule as mm
import platform

# Import only the person1 dictionary from the module
# from mymodule import person1

mymodule.greeting("Tom")

a = mymodule.person1["age"]
print(a)

mm.greeting("Sarah")

# built-in modules
x = platform.system()
y = platform.python_version()
print(x)
print(y)


# list module functions
x = dir(platform)
print(x)
