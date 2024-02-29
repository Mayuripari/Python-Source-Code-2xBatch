# set subset()
set1 = {1, 2, 3, 4, 5}
set2 = {2, 3, 4}
subset = set2.issubset(set1)
print(subset)  # True

set2 = set(["TheTestingAcademy", "the", "TheTestingAcademy."])
print(set2)
for i in set2:
    print(i)

set3 =([1, 2, 3, 4, 5, 6,
        7, 8, 9, 10, 11, 12])
print(set3)
set3.remove(5)   # remove 5 from set
set3.remove(6)   # remove 6 from set
print(set3)
print(len(set3))

