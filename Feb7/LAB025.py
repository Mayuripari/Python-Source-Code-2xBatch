# string concatenation
name1 = "hello "
name2 = "world"
name3 = name1 + name2
print(name3)
print("-----------------")
name = "mayuri"
age = 65
# r = name + age  # TypeError: can only concatenate str (not "int") to str
r = name + str(age) # changed the type from int to str
print(r)
print("-----------------")
g = "hey"
g += "world"
print(g)
