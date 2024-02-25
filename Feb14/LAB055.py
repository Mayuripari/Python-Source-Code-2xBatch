# *args and **kargs
# *args = any number of arguments you can give
# *args is nothing but list

def sum(*args):
    for i in args:
        print(i, end=" ")


sum(1)
sum(1, 2, 3, 4)
sum(10, 20, 30, 40, 50, 60, 70)
