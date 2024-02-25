# continue - continue in the loop

for num in range(1, 10):
    if num % 2 == 0:
        print(f"even number : {num}")
        continue
    print(f"odd number : {num}")  # this line is not in if loop. its in for loop
