# Set is a collection which is unordered and unindexed. No duplicate members.
# You cannot access items in a set by referring to an index or a key

# methods
# add()	Adds an element to the set
# clear()	Removes all the elements from the set
# copy()	Returns a copy of the set
# difference()	Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard()	Remove the specified item
# intersection()	Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not
# pop()	Removes an element from the set
# remove()	Removes the specified element
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	Return a set containing the union of sets
# update()	Update the set with the union of this set and others

myset = {"apple", "banana", "cherry"}
print(myset)

# alternative way to create
thisset = set(("apple", "banana", "cherry"))    # note the double round-brackets
print(thisset)

# ignores duplicates
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# length
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

# loop
thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)

# exists

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

# add (Once a set is created, you cannot change its items, but you can add new items.)
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# join
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# merge sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# merge any iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

# remove/discard

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

# or

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

# remove last item
# (Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.)
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

# clear/empty
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

# delete set completely

thisset = {"apple", "banana", "cherry"}

del thisset

# print(thisset) NameError: name 'thisset' is not defined

# keep/find all duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

# keep all values that exist in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

# keep everything except the duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

# return a set that contains all items from both sets, except items that are present in both:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)
