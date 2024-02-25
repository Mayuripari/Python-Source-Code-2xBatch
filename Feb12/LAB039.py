# Break
# break-kick out of the loop, break from thr loop
for counter in range(1, 10):
    if counter == 5:
        break
    print(counter)
print("outside of the loop")

print("-------------")

for i in range(1, 10):
    print(i)
    if i == 5:
        break
print("Out of the loop")
