class Account:
    def __init__(self, id, balance, annualInterestRate):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate

    def getId(self):
        return self.__id

    def getBalance(self):
        return self.__balance

    def getAnnualInterestRate(self):
        return self.__annualInterestRate

    def setId(self, id):
        self.__id = id

    def setBalance(self, balance):
        self.__balance = balance

    def setAnnualInterestRate(self, rate):
        self.__annualInterestRate = rate

    def getMonthlyInterest(self):
        monthlyInterestRate = self.__annualInterestRate / 12 / 100
        return self.__balance * monthlyInterestRate

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

# Test program
accounts = []
for id in range(0, 10):
    accounts.append(Account(id, 100, 0))
# account = Account(1122, 20000, 4.5)

# account.withdraw(2500)
# account.deposit(3000)

# print(f"Account ID: {account.getId()}")
# print(f"Balance: ${account.getBalance():.2f}")
# print(f"Monthly Interest Rate: {account.getAnnualInterestRate() / 12}%")
# print(f"Monthly Interest: ${account.getMonthlyInterest():.2f}")


while True:
    id = eval(input("Enter an account id: "))
    if id<1 or id>9:
        print("Invalid ID")
        continue

    account = accounts[id-1]
    while True:
        print(f"\n\nMain menu1: check balance\n"
                f"2: withdraw\n"
                f"3: deposit\n"
                f"4: exit\n")
        operation = eval(input("Enter a choice:"))

        match operation:
            case 1:
                print(f"Balance: ${account.getBalance():.2f}")
            case 2:
                ammount = eval(input("Enter an amount to withdraw: "))
                account.withdraw(ammount)
            case 3:
                deposit = eval(input("Enter an amount to deposit: "))
                account.deposit(deposit)
            case 4:
                break