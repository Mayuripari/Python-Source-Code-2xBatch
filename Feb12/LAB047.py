# match case for browser
browser = input("Enter the browser name:\n")
browser = browser.lower()   # the user input converts from Capital to small

match browser:
    case "chrome":
        print("chrome code executed")
    case "Firefox":
        print("FF code executed")
    case _:
        print("Other browser")
