# Constructor
class Car:
    name = None
    make = None
    model = None

    def __init__(self, o_name, o_make, o_model):  # this f(n) is called automatically when object is created
        self.name = o_name
        self.make = o_make
        self.model = o_model

    def start_engine(self):
        print("Start a car with name", self.name)
        print("Start a car with make", self.make)
        print("Start a car with model", self.model)


Lamborgini = Car(o_name="Lamborgini", o_make="V2",o_model="2024")
Lamborgini.start_engine()

XUV = Car(o_name="XUV", o_make="V1", o_model="2023")
XUV.start_engine()