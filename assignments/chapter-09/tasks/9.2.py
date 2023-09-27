import tkinter as tk

Label1 = tk.Label(text="investmentAmount: ")
Label2 = tk.Label(text="years: ")
Label3 = tk.Label(text="annualInterestRate: ")
Label4 = tk.Label(text="futureValue: ")

Value1 = tk.StringVar()
Value2 = tk.StringVar()
Value3 = tk.StringVar()
Value4 = tk.StringVar()

Entry1 = tk.Entry()
Entry2 = tk.Entry()
Entry3 = tk.Entry()
Entry4 = tk.Entry()

Label1.grid(row=0, column=0)
Label2.grid(row=1, column=0)
Label3.grid(row=2, column=0)
Label4.grid(row=3, column=0)

Entry1.grid(row=0, column=1)
Entry2.grid(row=1, column=1)
Entry3.grid(row=2, column=1)

Output = tk.Label(text="0")
Output.grid(row=3, column=1)


def calculate():
    Output.config(text=str(
        float(Entry1.get()) * (1 + float(Entry3.get()) / 1200) ** (float(Entry2.get()) * 12)
    ))


Button1 = tk.Button(text="Calculate", command=calculate)
Button1.grid(row=4, column=1)

tk.mainloop()
