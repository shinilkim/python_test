from classes.Sample import Sample, MyData

sample = Sample()
sample.hello()

a = MyData('shinil.kim',41)
a.sayHello()

# Polymorphism with a function
class Bear(object):
    def sound(self): print("Groarrr")
class Dog(object):
    def sound(self): print("Woof woof!")
def makeSound(animalType): animalType.sound()

bearObj = Bear()
dogObj = Dog()

makeSound(bearObj)
makeSound(dogObj)

