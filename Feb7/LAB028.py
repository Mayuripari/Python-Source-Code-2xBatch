#  HW - Feb 7 - Task 2
# Calculate square and cube of a number

num = int(input("Enter any number : "))
Sq = num * num
cube = num * num * num
print(f"Square={Sq}\nCube={cube}")

print("---------------OR-----------")
import math
num1 = int(input("Enter any number"))
sq = math.pow(num1,2)
print(sq)
cube = math.pow(num1, 3)
print(cube)
sq1 = num1 ** 2
print(sq1)
cube1 = num1 ** 3
print(cube1)
sqrt = math.sqrt(num1)
print(sqrt)
cube_root = math.cbrt(num1)
print(cube_root)