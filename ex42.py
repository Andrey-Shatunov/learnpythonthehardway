## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    def run(self):
        print "I can run"
    def ear(self):
        print "I eat"

## Dog is Animal
class Dog(Animal):

    def __init__(self, name):
        ## ??
        self.name = name
    def bark(self):
        print "I can bark"

## Cat is Animal
class Cat(Animal):

    def __init__(self, name):
        ## ??
        self.name = name
    def mew(self):
        print "I can mew"

##  Person is-a object
class Person(object):

    def __init__(self, name):
        ## ??
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None
        self.animals = []
        
    def speak(self):
        print "I can speak"
    def get_animals(self):
        for i in self.animals:
            print "I have %r " %i.name
            
## Employee is Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is Fish
class Salmon(Fish):
    pass

## Halibut is Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")
rover.run()
## Satan is cat
satan = Cat("Satan")

## Mary is Person
mary = Person("Mary")

## Mary has-a cat
mary.pet = satan
mary.animals.append(satan)
mary.animals.append(rover)
mary.get_animals()
## Frank is Employee
frank = Employee("Frank", 120000)

## Frank has dog
frank.pet = rover

## flipper is Fish
flipper = Fish()

## crouse is Salmon
crouse = Salmon()

## hary is Halibut
harry = Halibut()
