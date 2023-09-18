def futureInvestmentValue(investmentAmount, monthlyInterestRate, years):
    return investmentAmount * (1 + monthlyInterestRate) ** (years * 12)

amount = eval(input("The amount invested: "))
annualInterestRate = eval(input("Annual interest rate: "))

print("Years\tFuture Value")
for i in range(1, 31):
    print(f"{i}\t{round(futureInvestmentValue(amount, annualInterestRate / 12 / 100, i), 2)}")
    