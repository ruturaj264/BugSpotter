class account():

    def __init__(self, amount):
        self.__balance = amount

    def debit(self, amount):
        self.__balance -= amount

    def credit(self, amount):
        self.__balance += amount

    
my_account = account(100)
my_account.debit(10)
my_account.credit(10)

