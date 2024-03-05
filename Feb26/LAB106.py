# 2.Inheritance
# Single Inheritance
class Father:

    __house = "Goa private house"
    gold = "5kg"
    def car(self):
        print("Dad's Lamborgini")

    def threeBHK(self):
        print("Dad's 3BHK house")

    def access_House(self,is_my_son):
        if is_my_son:
            print(self.__house)


class Son(Father):
    pass


Mayur = Son()
Mayur.car()
Mayur.threeBHK()
print(Mayur.gold)
Mayur.access_House(True)