# f() performed on list -Part4
# 12. indexation
square = [1, 4, 9, 16, 25]
# index = [0,1,2,3,4]
# reverse index = [-5,-4,-3,-2,-1]
print(square[-1])  # reverse indexation
print(square[0])
print(type(square))

# 13. not list - check if the list is empty or not empty
my_list = []
if not my_list:
    print("empty")
else:
    print("not empty")

# 14. pop() - pop will remove the index value/element from list
print(square.pop(1))
print("my list after pop function:", square)
