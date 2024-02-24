# Take 2 numbers and add them
# Step1- Take in1put
# Step2- sum

num1 = input("Enter 1st number")
num2 = input("Enter 2nd number")
print(num1)
print(num2)
print(type(num1))
num3 = num1 + num2
print(num3)
# Here num1 and num2 are string type so its getting concatenation
# concat= combine/join num1 and num2, so we are changing the type of num1,num2
# change integer type for sum operation
# use int function- int() to change from str
num4 = int(num1) + int(num2)
print(num4)
print(type(num4))
