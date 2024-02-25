# class- Car
# Objects- Tesla, Lamborgini

class Car:
    model = None
    name = None
    year = None
    color = None
    engine = None

    def car_drive(self):
        print("I am driving: " + self.name)

    def car_break(self):
        print("Break")

    def car_engine(self):
        print("engine")


ref_obj1 = Car()
ref_obj2 = Car()

ref_obj1.name ="Tesla"
ref_obj2.name = "Lamborgini"

ref_obj1.car_drive()
ref_obj2.car_drive()