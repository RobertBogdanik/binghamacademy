# amount = 10000
# years = 5
#
# interest = 5.0
# while interest < 8.0:
#     # annualInterestRate = eval(input("Enter annual interest rate, e.g., 7.25: "))
#     monthlyInterestRate = interest / 1200
#
#     numberOfYears = years
#     loanAmount = amount
#
#     monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
#     totalPayment = monthlyPayment * numberOfYears * 12
#     interest += 1/8
#     print(interest, monthlyPayment, totalPayment)

import tkinter as tk

window = tk.Tk()
window.geometry("500x400")

top = tk.Frame(window)
label1 = tk.Label(top, text="Loan Amount")
label2 = tk.Label(top, text="Years")

years = tk.IntVar()
amount = tk.IntVar()
years.set(5)
amount.set(10000)

entry1 = tk.Entry(top, textvariable=amount)
entry2 = tk.Entry(top, textvariable=years)

label1.pack(side="left")
entry1.pack(side="left")
label2.pack(side="left")
entry2.pack(side="left")

top.pack(side="top")

result = tk.Frame(window)
tk.Label(result, text="Interest Rate").grid(row=0, column=0)
tk.Label(result, text="Monthly Payment: ").grid(row=0, column=1)
tk.Label(result, text="Total Payment: ").grid(row=0, column=2)

interest = 5.0
row = 1
while interest < 8.0:
    monthlyInterestRate = interest / 1200

    numberOfYears = years.get()
    loanAmount = amount.get()

    monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
    totalPayment = monthlyPayment * numberOfYears * 12
    interest += 1/8
    tk.Label(result, text=f"{interest}").grid(row=row, column=0)
    tk.Label(result, text=f"{monthlyPayment}").grid(row=row, column=1)
    tk.Label(result, text=f"{totalPayment}").grid(row=row, column=2)

    row += 1

result.pack(side="top")

window.mainloop()
