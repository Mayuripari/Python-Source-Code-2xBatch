# filter(function, iterable)
# function: A function that returns True or False.
# iterable: An iterable object such as a list, tuple, set, etc., whose elements will be filtered based on the function.
number = [1, 2, 3, 4, 5, 6, 7]
even_num = filter(lambda x: x % 2 == 0, number)  # Filter() returns only True here
print(list(even_num))

print("-----------------------------------")


def even_numbers(num):
    return num % 2 == 0


result = filter(even_numbers, number)
print(list(result))
