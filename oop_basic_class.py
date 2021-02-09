class Person:
    # creates class attribute for our 'Person'
    # every new person we create will be a 'homo sapien'
    species = "homo sapiens"

    # add init with parameters for our class
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    # method with attributes passed with return statement with .format
    def description(self):
        return "{} is {} years old and is {} feet tall".format(self.name, self.age, self.height)

    # instance method add parameter to do what you want it to
    def speak(self, sound):
        return "{} says {}.".format(self.name, sound)

    # instance methods that changes our init parameters specified
    def birthday(self):
        self.age += 1

    def grow(self):
        self.height += 1


# create new vars followed with class name and our parameters
blake = Person("Blake", 21, 6)
ap = Person("AP", 21, 6)

# print formatted print with method call
print(blake.description())
print(blake.speak("get to work"))
print(ap.speak("I am getting to work Blake"))

# birthday/grow function doesnt return anything it changes our values
# so we call our function and print the return method we're changing
blake.birthday()
print(blake.description())
blake.grow()
print(blake.description())
