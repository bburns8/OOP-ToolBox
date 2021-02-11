# To achieve composition you can instantiate other objects in the class
# then use those instances. For example in the below example we instantiate
# the Rocket class using self.rocket and then using self.rocket in the method get_maker.


class MarsRoverComp():
    def __init__(self, name, distance, maker):
        self.rocket = Rocket(name, distance) # instantiating the base

        self.maker = maker

    def get_maker(self):
        return "%s Launched by %s" % (self.rocket.name, self.maker)


if __name__ == "__main__":
    z = MarsRover("mars_rover2", "till Mars", "ISRO")
    print(z.launch())
    print(z.get_maker())