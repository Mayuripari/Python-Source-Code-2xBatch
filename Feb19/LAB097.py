# class - we are using self here to call the class variables
class Car:
    color = None
    model = None

    def car_details(self):
        print("Your car details are", self.color, self.model)


car_color = input("Enter car color : ")
car_model = input("Enter car model : ")

objref = Car()
objref.color = car_color
objref.model = car_model
car1 = objref.car_details()
car2 = objref.car_details()

