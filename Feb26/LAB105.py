class Password:
    def __init__(self, password):
        self.__password = "Hacker123"  # private variable

    # f(n) and GET and SET
    def get_password(self, is_auth):
        if is_auth:
            print(self.__password)
        else:
            print("You are not authenticated")

    def set_password(self, password):
        if len(password) > 10:
            self.__password = password
            print(self.__password)
        else:
            print("Not allowed, weak password")


pwd = Password("Hacker123")
pwd.get_password(False)
pwd.set_password("127677888888")
