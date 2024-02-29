# multiple assignment in tuple
x = 10
x, y, z = (3, 4, 5)
a, b = 12, 23

# Nested tuple
h1 = ("batman", "spiderman")
h2 = ("wonder woman", "diana prince")
h3 = (h1, h2)
print(h3)
print(h3[0])  # ("batman", "spiderman")
print(h3[1])  # ('wonder woman', 'diana prince')
print(h3[0][1]) # spiderman -particular element to print
