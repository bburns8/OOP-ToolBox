class Skier:
    # create class attribute for skier
    type = 'skier'

    # init method with unique instance attributes set to our parameters
    def __init__(self, name, brand, skill):
        self.name = name
        self.brand = brand
        self.skill = skill

    # instance methods that returns a formatted string with skiers attributes brought in
    def shred(self):
        return '{} is sponsored by {} and is a {} skier'.format(self.name, self.brand, self.skill)

    def flip(self, backy):
        print('{} is going to throw a {}'.format(self.name, backy))


# create a subclass snowboarder that inherits parent class Skier's attributes
class Snowboarder(Skier):
    # redefine our class attribute (uses this not our parent)
    type = 'snowboarder'

    def shred(self):
        return '{} is sponsored by {} and is a {} snowboarder'.format(self.name, self.brand, self.skill)


# create new var pointing to our skier class
blake = Skier('Blake', 'Crosson', 'expert')
print(blake.shred())
blake.flip("back-flip")

# create snowboarder var pointing to our child class with parameters you want to pass
zandar = Snowboarder('Zandar', 'LibTech', 'Expert')
print(zandar.shred())
