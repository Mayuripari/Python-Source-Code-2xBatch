# how to find a particular key is exist or not
my_dict = {'a': 2, 'b': 3, 'c': 6}

for k, v in my_dict.items():
    if k == 'b':
        print("b is found")

print("----------------------")
op = 'b' in my_dict
print(op)