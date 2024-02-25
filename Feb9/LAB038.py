# HW- Leap Year
# Condition - Every year that is exactly divisible by four is a leap year,
# except for years that are exactly divisible by 100,
# but these centurial years are leap years if they are exactly divisible by 400
num = int(input("Enter the Year: "))
if num % 4 == 0:
    print("This is Leap Year")
elif num % 100 == 0 and num % 400 == 0:
    print("This is Leap Year")
else:
    print("This is not a leap year")
