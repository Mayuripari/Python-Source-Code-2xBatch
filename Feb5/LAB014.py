# strings length
# index start from 0 and length starts from 1
name = "batman"
print(name[0])
print(name[4])
# print(name[6])     # IndexError: string index out of range
print(len(name))   # length= 6(starts from 0 to 5)
print("--------------------")
print(len(name)-1)
print(name[len(name)-1])


