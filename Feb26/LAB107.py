# Multilevel Inheritance
class GrandFather:
    def home1(self):
        print("Grandfather's 3BHK house in native")


class Father(GrandFather):
    def home2(self):
        print("Father's house in Goa")


class Son(Father):
    def home3(self):
        print("Son having house in Bangalore")


Mayur = Son()
Mayur.home1()
Mayur.home2()
Mayur.home3()
print("------------------")
myFather = Father()
myFather.home1()
myFather.home2()
print("------------------")
myGrandpa = GrandFather()
myGrandpa.home1()