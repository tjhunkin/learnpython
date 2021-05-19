# This is a comment.
x = 4           # x is of type int
x = "Sally"     # x is now of type str
y = "Hello, World!"

# case sensitive
a = 4
A = "Sally"
# A will not overwrite a

"""
This is hack to comment
on
multiple
lines
"""

print(x)
print(y)

# casting
x = str(3)      # x will be '3'
y = int(3)      # y will be 3
z = float(3)    # z will be 3.0

print(x)        # <type 'str'>
print(y)        # <type 'int'>
print(z)        # <type 'float'>

print(type(x))
print(type(y))
print(type(z))

# multiple variables, multiple values
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# one value, multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# unpacking variables
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
