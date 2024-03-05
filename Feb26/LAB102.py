# Public, Protected, Private variables and methods
# we cant access private or protected functions and variables directly.
# we can access the functions thr private methods/functions, created within the same class
class MyClass:
    def __init__(self, name):
        self.name = "Sana"

    def public_function(self):
        print("This is public fucntion")

    def __private_function(self):
        print("This is private function")

    def public_calls_privatefunction(self):
        self.__private_function()


a = MyClass("Mayuri")
a.public_function()
a.public_calls_privatefunction()
