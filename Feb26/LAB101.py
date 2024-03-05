# OOps concept
# Class- Blueprint to create something
# Object -Real time entity created from Class
# OOps- Every class and object created have some features
# 1.Encapsulation
# Functions are closed within a single blueprint
# Wrapping or binding the data variables with the methods
# we cant access the private and protected methods and variables directly

class Car:
    name = None

    def __init__(self, name):
        self.name = name

    def printName(self):
        print(self.name)


XUV = Car("XUV")
XUV.printName()
print(XUV.name)