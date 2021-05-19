# A tuple is a collection which is ordered and unchangeable.

thistuple = ("apple", "banana", "cherry")   # round brackets
print(thistuple)

# length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

thistuple = ("apple",)
print(type(thistuple))

# NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# other way to create a tuple
thistuple = tuple(("apple", "banana", "cherry"))    # note the double round-brackets
print(thistuple)

# negative indexing

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

# range

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

# exclude

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

# from value to end

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

# exists

thistuple = ("apple", "banana", "cherry")

if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

# change (convert the tuple into a list, change the list, and convert the list back into a tuple.)

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# add items (convert the tuple into a list, add to the list, and convert the list back into a tuple.)
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# remove items (convert the tuple into a list, remove from list, and convert the list back into a tuple.)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

# delete tuple

thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple)    #this will raise an error because the tuple no longer exists


# unpack
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# unpack unmatched
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

# unpack mid

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

# apple
# ['mango', 'papaya', 'pineapple']
# cherry
