balance, annualInterestRate = eval(input("Enter balance and interest rate (e.g., 3 for 3%): "))
interest = balance * (annualInterestRate / 1200)
print(f"The interest is {round(interest, 5)}")
