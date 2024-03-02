# swap 2 numbers
num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
num3 = 0
num3 = num1
num1 = num2
num2 = num3
print("values after swap\n", "num1 :", num1, "num2: ", num2)
print("------------------------------")
x = int(input("Enter number1: "))
y = int(input("Enter number2: "))
x, y = y, x
print("values after swap: \n", x, y)