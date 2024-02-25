# Class and object

class Calculator:
    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


obj_ref = Calculator()
result1 = obj_ref.sum(3, 6)
result2 = obj_ref.sub(10, 20)
result3 = obj_ref.mul(3, 3)
result4 = obj_ref.div(25, 5)

print(result1, result2, result3, result4)
