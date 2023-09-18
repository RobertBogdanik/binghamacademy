class Account:
    def __init__(self, id=0, balance=100, annualInterestRate=0):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = 0

    def get_id(self):
        return self.__id

    def get_balance(self):
        return self.__balance

    def get_annualInterestRate(self):
        return self.__annualInterestRate

    def getMonthlyInterestRate(self):
        return self.__annualInterestRate / 12

    def getMonthlyInterest(self):
        return self.__balance * self.getMonthlyInterestRate() / 100

    def withdraw(self, amount):
        self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount

    def __str__(self):
        return f"Account ID: {self.__id}\nBalance: {self.__balance}\nMonthly Interest Rate: {self.getMonthlyInterestRate()}\nMonthly Interest: {self.getMonthlyInterest()}"

account = Account(1122, 20000, 4.5)
account.withdraw(2500)
account.deposit(3000)
print(account)
