class SecureClass:
    def submit(self):
        self.__username = "admin"
        self.__password = "123"
        self.header = "VWO login"


chrome = SecureClass()
chrome.submit()
print(chrome.header)   # public variable
