amount = eval(input("Enter an amount, for example, 11.56: "))

amount = str(amount)
amount = amount.replace(".", "")
amount = amount[:-2] + "." + amount[-2:]
amount = float(amount)

remainingAmount = int(amount * 100)

# 1
numberOfOneDollars = remainingAmount // 100
remainingAmount = remainingAmount % 100

# 0.25
numberOfQuarters = remainingAmount // 25
remainingAmount = remainingAmount % 25

# 0.1
numberOfDimes = remainingAmount // 10
remainingAmount = remainingAmount % 10

# 0.5
numberOfNickels = remainingAmount // 5
remainingAmount = remainingAmount % 5

# 0.1
numberOfPennies = remainingAmount

print("Your amount", amount, "consists of\n",
    "\t", numberOfOneDollars, "dollars\n", "\t", numberOfQuarters, "quarters\n",
    "\t", numberOfDimes, "dimes\n",
    "\t", numberOfNickels, "nickels\n",
    "\t", numberOfPennies, "pennies")

