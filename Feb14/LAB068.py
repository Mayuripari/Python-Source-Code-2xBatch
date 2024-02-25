# reverse the name
name = input("Enter your name:")
reverse = ""
for i in range(len(name) - 1, -1):
    reverse = name[i] + reverse

print("name:", reverse)
