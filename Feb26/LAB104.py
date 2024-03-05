class BankAccount:
    def __init__(self):
        self.balance = 0
        self.__private_var = 100

    def deposit(self, amount):
        self.balance += amount

    def _withdraw(self, amount):
        self.balance -= amount

    def __show_Balance(self):
        print("Your balance is", self.balance)

    def if_you_authenticated(self, flag):
        if flag:
            self.__show_Balance()
        else:
            print("You are not authenticated to see balance")

    def bank_manager(self, amount):
        self._withdraw(amount=amount)


jp_morganBank = BankAccount()
jp_morganBank.deposit(1000)
jp_morganBank.bank_manager(500)
jp_morganBank.if_you_authenticated(True)
jp_morganBank.if_you_authenticated(False)
