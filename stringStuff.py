# specific character in string (string as array)
a = "Hello, World!"
print(a[1])

# loop string
for x in "banana":
    print(x)

# length of string
print(len(a))

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

txt = "The best things in life are free!"
if "expensive" not in txt:
    print("Yes, 'expensive' is NOT present.")

# slicing
b = "Hello, World!"
print(b[2:5])

# slicing from start
b = "Hello, World!"
print(b[:5])

# slicing to end
b = "Hello, World!"
print(b[2:])

# negative indexing

b = "Hello, World!"
print(b[-5:-2])

# uppercase
a = "Hello, World!"
print(a.upper())

# lowercase
a = "Hello, World!"
print(a.lower())

# trim
a = " Hello, World! "
print(a.strip())    # returns "Hello, World!"

# replace
a = "Hello, World!"
print(a.replace("H", "J"))

# split
a = "Hello, World!"
print(a.split(","))     # returns ['Hello', ' World!']

for x in a.split(","):
    print(x)

# concatenate
a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

# string format
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname="Ford", model="Mustang"))

txt = "For only {price:.2f} dollars!"
print(txt.format(price=49))

# escape
txt = "We are the so-called \"Vikings\" from the north."
