# The self parameter is a reference to the current instance of the class,
# and is used to access variables that belong to the class.
# It does not have to be named self ,
# you can call it whatever you like, but it has to be the first parameter of any function in the class

class MyClass:
    x = 5


p0 = MyClass()
print(p0.x)


class Person:
    def __init__(self, name, age):  # constructor
        self.name = name
        self.age = age

    def printName(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)

# p1.age = 40

print(p1.name)
print(p1.age)
p1.printName()

# delete properties
del p1.age

# delete object
del p1


# child class inheritance
# Note: Use the pass keyword when you do not want to add any other properties or methods to the class.
# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
# Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.

class Student(Person):
    pass


x = Student("Mike", "Olsen")
x.printName()

# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function


class AnotherStudent(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)


x = AnotherStudent("Tom", "Hunkin")
x.printName()


# Python also has a super() function that will make the child class inherit all
# the methods and properties from its parent:
# By using the super() function, you do not have to use the name of the parent element,
# it will automatically inherit the methods and properties from its parent.

class YetAnotherStudent(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)


x = YetAnotherStudent("Sarah", "Hunkin")
x.printName()


class WootAnotherStudent(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def printName(self):
        print("Welcome", self.name, self.name, "to the class of", self.graduationyear)


y = WootAnotherStudent('Jess', 'Hunkin', 2021)

y.printName()
