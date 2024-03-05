# Constructor
class Person:
    # Class variables/Instance variables
    name = "Mayuri"
    age = None

    def walk(self):
        a = 10  # Local variable
        print("My name is ", self.name)
        print("my age is", self.age)
        print(a)


Aniket = Person()
Aniket.walk()

Mayuri = Person()
Mayuri.walk()