# To achieve composition you can instantiate other objects in the class
# then use those instances. For example in the below example we instantiate
# the Rocket class using self.rocket and then using self.rocket in the method get_maker.


class Rocket:
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance

    def launch(self):
        return "%s has reached %s" % (self.name, self.distance)


class MarsRover(Rocket):  # inheriting from the base class
    def __init__(self, name, distance, maker):
        Rocket.__init__(self, name, distance)
        self.maker = maker

    def get_maker(self):
        return "%s Launched by %s" % (self.name, self.maker)


if __name__ == "__main__":
    x = Rocket("Simple Rocket", "till stratosphere")
    y = MarsRover("Mars Rover", "till Mars", "ISRO")
    print(x.launch())
    print(y.launch())
    print(y.get_maker())


# utilizing composition example
class MarsRoverComp:
    def __init__(self, name, distance, maker):
        self.rocket = Rocket(name, distance)  # instantiating the base

        self.maker = maker

    # this uses the %s method to pass objects as string instead of the .format
    def get_maker(self):
        return "%s Launched by %s" % (self.rocket.name, self.maker)


if __name__ == "__main__":
    z = MarsRover("Mars Rover 2", "till Mars", "ISRO")
    print(z.launch())
    print(z.get_maker())
