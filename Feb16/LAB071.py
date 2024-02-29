import math

list1 = [4, 9, 16, 25, 100]


def sq_num(num):
    return math.sqrt(num)


#    return math.cbrt(num)


result1 = list(map(sq_num, list1))
print(result1)
