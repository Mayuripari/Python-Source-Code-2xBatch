# search in tuple - in()
cities = ("Paris", "London", "Los angeles", "Tokyo" )
print("Paris" in cities)
print("Moscow" in cities)

# string is also immutable
name = "Mayuri"
name[0] = "A"    # TypeError: 'str' object does not support item assignment
print(name)