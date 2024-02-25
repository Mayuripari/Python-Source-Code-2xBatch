# function can work with any kind of data types
# Program for sum of 2 numbers

def sum_of_two(a, b):
    return a + b


result1 = sum_of_two(10, 100)
print(result1)

result2 = sum_of_two(1.5, 6.8)
print(result2)

result3 = sum_of_two("Mayuri", "Parit")
print(result3)

result4 = sum_of_two("Mayuri", 345)
print(result4)  # TypeError: can only concatenate str (not "int") to str
