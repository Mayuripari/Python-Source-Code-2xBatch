# Reverse the number -598761- 6digit
def rev_num(*number):
    for i in number:
        if i % 1 == 0:
            print(i)
        elif i % 10 == 0:
            print(i)
        elif i % 100 == 0:
            print(i)
        elif i % 1000 == 0:
            print(i)
        elif i % 10000 == 0:
            print(i)
        else:
            i % 100000 == 0
            print(i)
    return i

number = 598761
result = rev_num(number)
print(result)