# map(function, iterable)
# function: The function to apply to each item in the iterable.
# iterable: An iterable object such as a list, tuple, set, etc., whose elements will be passed to the function.
def sq_num(num):
    return num ** 2


number = [1, 2, 3, 4, 5]
# result = sq_num(2)
# print(result)
sq_numbers = list(map(sq_num, number))
print("result=", sq_numbers)
