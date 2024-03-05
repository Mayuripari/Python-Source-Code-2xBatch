# Selenium automation
# automate a page for login
class VMloginPage:
    email = None
    password = None

    def __init__(self, email, password):   # parameterized constructor always
        self.email = email
        self.password = password

    def loginconfirm(self):
        if self.password == "Pass123":
            print("You are allowed to Enter")
        else:
            print("Invalid credentials")


Mayuri = VMloginPage(email="parit@com", password="pass12345")
Mayuri.loginconfirm()

print("----------------------")

Mira =VMloginPage(email="mira@com",password="Pass123")
Mira.loginconfirm()

print(id(Mayuri))  # ID means location of object in memory
print(id(Mira))
