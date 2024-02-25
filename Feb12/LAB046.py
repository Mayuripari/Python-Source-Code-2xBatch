# Match Case - same as switch in Java
# No BREAK is needed in case of MATCH and CASE
number = int(input("Enter a number between 1-6\n"))
match number:
    case 1:
        print("You have entered 1")
    case 2:
        print("You have entered 2")
    case 3:
        print("You have entered 3")
    case 4:
        print("You have entered 4")
    case 5:
        print("You have entered 5")
    case 6:
        print("You have entered 6")
    case _:
        print("No idea")


