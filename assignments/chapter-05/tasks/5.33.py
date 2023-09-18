amount = eval(input("Enter an amount, for example, 11.56: "))
annualInterestRate = eval(input("Enter annual interest rate, for example, 8.25: "))
numberOfMonths = eval(input("Enter number of months, for example, 5: "))

monthlyInterestRate = annualInterestRate / 12 / 100
accountValue = amount

print("Month\tCD Value")
for i in range(numberOfMonths):
    accountValue = accountValue + (accountValue * annualInterestRate) / 1200
    print(f"{i+1}\t{round(accountValue, 2)}")
