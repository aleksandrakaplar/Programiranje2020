# example 01 : Defining a class
# Convention when writing class name is CapitalizedWords
class Parrot:
    # pass - placeholder where code will go
    pass


# example 02: defining attributes
class Duck:
    # class attribute
    animal = "bird"

    # defining properties
    # __init__ is a method that will set initial states of object type Duck
    # this method is called when we instantiate a Duck object
    def __init__(self, species, weight):
        # instance attribute species
        self.species = species
        # instance attribute weight
        self.weight = weight


# example 03: defining methods
class Horse:

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    # instance method, a method that is defined in a class
    def description(self):
        return f"{self.name} is a {self.breed}, {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


if __name__ == '__main__':
    print("======Example 01======")
    # instantiating a parrot object
    myParrot = Parrot()

    print('print memory address where object myParrot is stored:')
    print(myParrot, '\n')

    yourParrot = Parrot()

    print('print memory address where object yourParrot is stored:')
    print(yourParrot, '\n')

    print("Are objects myParrot and yourParrot the same object?")
    print(myParrot == yourParrot, '\n')

    print("======Example 02======")
    # return error
    # mallardDuck = Duck()

    mallardDuck = Duck('Mallard', 1.6)

    print("The mallardDuck object is a species of ", mallardDuck.species, "that can weight ", mallardDuck.weight,
          ".This is a ", mallardDuck.animal)

    shovelerDuck = Duck('Northern shoveler', 0.6)
    print("The shovelerDuck object is a species of ", shovelerDuck.species, "that can weight ", shovelerDuck.weight,
          ".This is a ", mallardDuck.animal)

    print("======Example 03======")
    horse = Horse("Thunder", "Thoroughbred", 3)
    print(horse.description())

    # sound = horse.speak("neigh")
    # print(sound)
    print(horse.speak("neigh"))
