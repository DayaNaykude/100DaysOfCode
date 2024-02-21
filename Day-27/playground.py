# *args
def add(*args):
    total = 0
    print(args)
    for num in args:
        total += num
    return total


# print(add(1, 3, 4, 5, 7))


# **kwargs

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


# print(calculate(2, add=3, multiply=5))


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.door = kwargs.get("door")


new_car = Car(make=True, door=2)
print(new_car.make)