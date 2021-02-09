class Person:
    description = "general person"

    # init method with instance attributes set to our parameters
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def speak(self):
        print("My name is {} and I am {} years old.".format(self.name, self.age))

    def eat(self, food):
        print("{} eats {}.".format(self.name, food))

    def action(self):
        print("{} spins.".format(self.name))


# create a class baby that inherits parent class Person
class Baby(Person):
    description = "baby"

    def speak(self):
        print("ba ba ba ba ba")

    def nap(self):
        print("{} takes a nap.".format(self.name))


person = Person("Steve", 20)
person.speak()
person.eat("pasta")
person.action()
# create baby var with parameters you want to pass
baby = Baby("Ian", 1)
baby.speak()
baby.eat("Baby food")
baby.action()

print(person.description)
print(baby.description)

