# Triangle
# side1 = side2 = side3 ---Equilateral Triangle
# side1 = side2 or side2 = side3 or side3 =side1 - Isosceles Triangle
# else --scalene Triangle
side1 = float(input("Enter side1 : "))
side2 = float(input("Enter side2 : "))
side3 = float(input("Enter side3 : "))
if side1 == side2 or side2 == side3 or side3 == side1:
    print("Isosceles Triangle")
elif side1 == side2 == side3:
    print("Equilateral Triangle")
else:
    print("scalene Triangle")

print("--------------------")

if side1 == side2 == side3:
    print("Equilateral Triangle")
elif side1 == side2 or side2 == side3 or side3 == side1:
    print("Isosceles Triangle")
else:
    print("scalene Triangle")
