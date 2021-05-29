class Car:
    def __init__(self):
        print("Engine started")
        self.name = "corolla"  # public variable

        # To create a private variable, you need to prefix double underscores with the name of the variable
        self.__make = "toyota"

        # To create a protected variable, you need to prefix a single underscore with the variable name
        self._model = 1999


car_a = Car()
print(car_a.name)
print(car_a.make)
