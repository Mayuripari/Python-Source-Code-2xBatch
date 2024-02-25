# class and objects in python

class Person:
    # Attributes - Data members
    name = None
    age = None
    Height = None

    # Behaviour - Methods
    def talk(self):
        print("Talk")

    def walk(self):
        print("Walk")


# objects - classname()
shree = Person()
shree.name = "Shreeram"
print(shree.name)
Vina = Person()
Vina.age = 15
print(Vina.age)
Pramod = Person()
Pramod.Height = "5.5"
print(Pramod.Height)

