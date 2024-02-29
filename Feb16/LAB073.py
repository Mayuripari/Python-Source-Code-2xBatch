# Tuple -immutable
# list- [], tuple- (), set- {}, dict- {}
my_list = [1, 2, 3, 4, 5]
my_list[0] = 21  # change the 1st element of list
print(my_list)

my_tuple = (11, 22, 33, 44, 55)
print(my_tuple)
print(type(my_tuple))
print(len(my_tuple))
# my_tuple[0] = 23    # TypeError: 'tuple' object does not support item assignment
# Type conversion
tuple1 = tuple(my_list)
print(tuple1)