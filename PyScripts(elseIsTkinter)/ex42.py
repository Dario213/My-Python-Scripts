#Animal is-a object
class Animal(object):
    pass

#Dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        #From self, get name attribute and set it to name
        self.name = name

#Cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        #From self, get name attribute and set it to name
        self.name = name

#Person is-a object
class Person(object):

    def __init__(self, name):
        #From self, get name attribute and set it to name
        self.name = name
        #Person has-a pet of some kind
        self.pet = None

#Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        #?? hmm, what is this strange magic?
        super(Employee, self).__init__(name)
        #From self, get the salary attribute and set it to salary
        self.salary = salary

#Fish is-a object
class Fish(object):
    pass

#Salmon is-a Fish
class Salmon(Fish):
    pass

#Halibut is-a Fish
class Halibut(Fish):
    pass

# rover is-a Dog
rover = Dog("Rover")
#satan is-a Cat
satan = Cat("Satan")
#mary is-a Person
mary = Person("Mary")

# From Mary get pet attribute and set it to Satan
mary.pet = satan
# Set frank to an instance of a class Employee
frank = Employee("Frank", 120000)
# From frank get pet attribute and set it to Rover
frank.pet = rover
#Set flipper to an instance of class Fish
flipper = Fish()
#Set  crouse to an instance of class Salmon
crouse = Salmon()
#Set harry to an instance of class Halibut
harry = Halibut()
