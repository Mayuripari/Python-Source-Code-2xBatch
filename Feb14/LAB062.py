# lambda Expression
# f(n)- function can be define in one line
# It will save memory

# normal function
# def double_mysalary(salary):
#    return salary * 2


# d_salary = double_mysalary(10000)
# print(d_salary)

# using lambda()
d_salary = lambda salary: salary * 2
print(d_salary(5000))
