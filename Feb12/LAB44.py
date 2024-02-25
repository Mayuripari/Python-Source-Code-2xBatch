# Factorial
# 3! = 3*2*1 = 6
# 5! = 5*4*3*2*1 = 120
num = int(input("Enter the number for the factorial : "))
if num < 0:
    print("Factorial is not possible")
elif num == 0:
    print("Factorial = 1")
else:
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
print(f"Factorial of {num} = {fact}")  # why it is saying fact is not defined?
