# List - collection of items(duplicate is allowed)
# f() performed on list -Part1
my_list = [1, 2, 3]     # indexing starts from 0,1,2
my_list2 = [1, True, 'Mayuri', 3.6]

# 1. Indexing
print("Element at index 0: ", my_list[0])

# 2.Changing element in list
my_list2[2] = 200
print("Element at index 2 after changing: ", my_list2[2])

# 3.append() -add element at the end of list
my_list.append(160)
print("list after appending: ", my_list)
my_list2.append("Mayuri")
print("list2 after appending: ", my_list2)