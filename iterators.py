# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon,
# meaning that you can traverse through all the values.

# Return an iterator from a tuple, and print each value:
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


# looping

mytuple = ("apple", "banana", "cherry")

for x in mytuple:   # The for loop actually creates an iterator object and executes the next() method for each loop.
    print(x)

# custom iteration


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            i = self.a
            self.a += 1
            return i
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
