# f() performed on list -Part3
my_list = [1, 333, 56, 897, 5, 88]

# 10. sort()
my_list.sort()   # sorting means put in ascending order
print("my list after sorting", my_list)

# 11. reverse()
my_list.reverse()
print("my list after reverse", my_list)

# heterogeneous data- sorting not allowed
my_list2 = [1, True, "k", 3.6, 11, 12]
my_list2.sort()
print("my list after sorting:", my_list2)  # TypeError: '<' not supported between instances of 'str' and 'bool'
