# Dict
my_details1 = dict(name="Mayuri", phone="1234567890", age=44, isMarried=True)
print(my_details1)
my_details2 = {"name": "Mayuri", "age": 44, "90": 32.32, "isMale": False, "Address": "MH"}
print(my_details2)
print(my_details2["90"])
print(my_details2.get(90))  # None
print(my_details2.get("90"))

# Keys cannot be duplicated
dict1 = {'a': 10, 'b': 14, 'c': 30, 'a': 25}
print(len(dict1))    # key 'a' is duplicate
print(dict1)
