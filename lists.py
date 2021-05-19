# List is a collection which is ordered and changeable. Allows duplicate members.

# methods
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

thisList = ["apple", "banana", "cherry"]
print(thisList)

# create new list
thisList = list(("apple", "banana", "cherry"))  # note the double round-brackets
print(thisList)
print(thisList[1])

# get last item
thisList = ["apple", "banana", "cherry"]
print(thisList[-1])

# range
thisList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thisList[2:5])

# negative range
thisList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thisList[-4:-1])

# exclude
thisList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thisList[:4])

# start from
thisList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thisList[2:])

# check if exists
thisList = ["apple", "banana", "cherry"]

if "apple" in thisList:
    print("Yes, 'apple' is in the fruits list")

# change value
thisList = ["apple", "banana", "cherry"]
thisList[1] = "blackcurrant"
print(thisList)

# change range
thisList = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thisList[1:3] = ["blackcurrant", "watermelon"]
print(thisList)

# insert item
thisList = ["apple", "banana", "cherry"]
thisList.insert(2, "watermelon")
print(thisList)

# append to end
thisList = ["apple", "banana", "cherry"]
thisList.append("orange")
print(thisList)

# extend a list with another list
thisList = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thisList.extend(tropical)
print(thisList)

# add any iterable object
thisList = ["apple", "banana", "cherry"]
thisTuple = ("kiwi", "orange")
thisList.extend(thisTuple)
print(thisList)

# remove item
thisList = ["apple", "banana", "cherry"]
thisList.remove("banana")
print(thisList)

# delete item
thisList = ["apple", "banana", "cherry"]
del thisList[0]
print(thisList)

# delete list
thisList = ["apple", "banana", "cherry"]
del thisList

# clear a list
thisList = ["apple", "banana", "cherry"]
thisList.clear()
print(thisList)

# remove via index
thisList = ["apple", "banana", "cherry"]
thisList.pop(1)
print(thisList)

# remove last item
thisList = ["apple", "banana", "cherry"]
thisList.pop()
print(thisList)

# loop
thisList = ["apple", "banana", "cherry"]
for x in thisList:
    print(x)
    
# loop index numbers
thisList = ["apple", "banana", "cherry"]
for i in range(len(thisList)):
    print(thisList[i])
    
# loop using while
thisList = ["apple", "banana", "cherry"]
i = 0
while i < len(thisList):
    print(thisList[i])
    i = i + 1
    
# loop using comprehension
thisList = ["apple", "banana", "cherry"]
[print(x) for x in thisList]\

# without list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = []

for x in fruits:
    if "a" in x:
        newList.append(x)

print(newList)

# with list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newList = [expression for item in iterable if condition == True]
newList = [x for x in fruits if "a" in x]   # get all values with a in it

print(newList)

# sort

thisList = ["orange", "mango", "kiwi", "pineapple", "banana"]
thisList.sort()
print(thisList)

thisList = [100, 50, 65, 82, 23]
thisList.sort()
print(thisList)

# reverse sort

thisList = ["orange", "mango", "kiwi", "pineapple", "banana"]
thisList.sort(reverse=True)
print(thisList)

# custom sort


def myfunc(n):
    return abs(n - 50)


thisList = [100, 50, 65, 82, 23]
thisList.sort(key=myfunc)
print(thisList)

# case-insensitive sort
thisList = ["banana", "Orange", "Kiwi", "cherry"]
thisList.sort(key=str.lower)
print(thisList)

# reverse

thisList = ["banana", "Orange", "Kiwi", "cherry"]
thisList.reverse()
print(thisList)

# copy
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# join lists

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# or

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)

# or

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

# multiply
list1 = ["a", "b", "c"]
print(list1 * 2)