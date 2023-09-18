monthlySavingAmount = eval(input("Enter the monthly saving amount: "))
annualInterestRate = eval(input("Enter the annual interest rate: "))
numberOfMonths = eval(input("Enter the number of months: "))

monthlyInterestRate = annualInterestRate / 12 / 100
accountValue = 0

for i in range(numberOfMonths):
    accountValue = (monthlySavingAmount + accountValue) * (1 + monthlyInterestRate)
    print(f"Month {i+1} account value is {round(accountValue, 2)}")

print(f"After the {numberOfMonths} month, the account value is {round(accountValue, 2)}")
