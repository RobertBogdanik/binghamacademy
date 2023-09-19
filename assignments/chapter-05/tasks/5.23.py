amount = 10000
years = 5

interest = 5.0
while interest < 8.0:
    # annualInterestRate = eval(input("Enter annual interest rate, e.g., 7.25: "))
    monthlyInterestRate = interest / 1200

    numberOfYears = years
    loanAmount = amount

    monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
    totalPayment = monthlyPayment * numberOfYears * 12
    interest += 1/8
    print(interest, monthlyPayment, totalPayment)
