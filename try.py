# the try block lets you test a block of code for errors.
# the except block lets you handle the error.
# the finally block lets you execute code, regardless of the result of the try- and except blocks.

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Execute if okay (else)")
finally:
    print("Execute no matter what (finally)")

print('-----------')

# The finally block, if specified, will be executed regardless if the try block raises an error or not.
try:
    print(x)
except:
    print("Something went wrong (except)")
finally:
    print("Execute no matter what (finally)")

print('-----------')

# multiple excepts
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

# try opening a file
f = open("demofile.txt")
try:
    f.write("Lorum Ipsum")
except:
    print("Something went wrong when writing to the file")
finally:
    f.close()

# raise an exception
x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")

# or

x = "hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed")


