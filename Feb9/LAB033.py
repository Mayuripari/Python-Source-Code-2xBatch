# Find the max between 3 numbers
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))
max_num = max(num1, num2, num3)
print(max_num)

print("--------------or by if condition------------")
if (num1 > num2) and (num1 > num3):
    print("num1 is greater", num1)
elif (num2 > num3) and (num2 > num3):
    print("num2 is greater", num2)
else:
    print("num3 is greater", num3)
