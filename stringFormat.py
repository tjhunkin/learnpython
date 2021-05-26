price = 49
txt = "The price is {} dollars"
print(txt.format(price))

# with two decimals
price = 49
txt = "The price is {:.2f} dollars"
print(txt.format(price))

# multiple variables
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# indexing variables
uantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# named indexes
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname="Ford",model="Mustang"))
