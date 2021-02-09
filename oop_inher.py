class Dog:
    species = "wolf"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return 'Hello my name is {} and I am {} years old.'.format(self.name, self.age)


class Puppy(Dog):
    species = 'wolf'

    def wimper(self):
        return '{} wimpers and wimpers in the crate'.format(self.name)

    def birthday(self):
        self.age += 1
        return 'Happy birthday {} you are now {} years old!'.format(self.name, self.age)

    def speak(self):
        return '{} says {}'.format(self.name)


henry = Dog('Henry', 10)
print(henry.speak())
baby_henry = Puppy('Baby Henry', 1)
print(baby_henry.wimper())
print(baby_henry.birthday())



