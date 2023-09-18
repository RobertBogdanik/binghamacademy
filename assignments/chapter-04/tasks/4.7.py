amount = eval(input("Enter an amount, for example, 11.56: "))

# Convert the amount to cents
remainingAmount = int(amount * 100)

# Find the number of one dollars
numberOfOneDollars = remainingAmount // 100
remainingAmount = remainingAmount % 100

# Find the number of quarters in the remaining amount
numberOfQuarters = remainingAmount // 25
remainingAmount = remainingAmount % 25

# Find the number of dimes in the remaining amount
numberOfDimes = remainingAmount // 10
remainingAmount = remainingAmount % 10

# Find the number of nickels in the remaining amount
numberOfNickels = remainingAmount // 5
remainingAmount = remainingAmount % 5

# Find the number of pennies in the remaining amount
numberOfPennies = remainingAmount

if numberOfOneDollars == 1:
    dollar = "dollar"
else:
    dollar = "dollars"

if numberOfQuarters == 1:
    quarter = "quarter"
else:
    quarter = "quarters"

if numberOfDimes == 1:
    dime = "dime"
else:
    dime = "dimes"

if numberOfNickels == 1:
    nickel = "nickel"
else:
    nickel = "nickels"

if numberOfPennies == 1:
    penny = "penny"
else:
    penny = "pennies"
    
print(f"Your amount {amount} consists of\n",
      f"\t{numberOfOneDollars} {dollar}\n",
      f"\t{numberOfQuarters} {quarter}\n",
      f"\t{numberOfDimes} {dime}\n",
      f"\t{numberOfNickels} {nickel}\n",
      f"\t{numberOfPennies} {penny}")
