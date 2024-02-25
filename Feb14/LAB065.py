# f() performed on list -Part2
my_list = [1, 2, 3]     # indexing starts from 0,1,2
my_list2 = [1, True, 'Mayuri', 3.6]

# 4. extend() -append is single element, extend is add list
my_list.extend([5, 6])
print("my list updated: ", my_list)

# 5. insert()
my_list.insert(1, "a")
print("my list updated: ", my_list)

# 6.remove()
my_list.remove('a')
print("my list after removing element: ", my_list)

# 7.copy()
list3 = my_list2.copy()
print("my list2 after copy:list3:", list3)

# 8.clear()
list3.clear()
print("list3 =", list3)

# 9. Index of element in list
print("index of element 3.6 in the list:", my_list2.index(3.6))  # answer is 3
print("index of element Mayuri in the list:", my_list2.index("Mayuri")) # answer is 2
