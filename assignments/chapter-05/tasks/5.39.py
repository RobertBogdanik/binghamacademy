salesAmount = eval(input("Enter sales amount: "))
commission_rate = 0
base_salary = 5000
commission = 0
total_salary = 0

if salesAmount >= 0.01 and salesAmount <= 5000:
    commission_rate = 0.08
elif salesAmount >= 5000.01 and salesAmount <= 10000:
    commission_rate = 0.10
elif salesAmount >= 10000.01:
    commission_rate = 0.12
else:
    print("Invalid input")
    exit()

commission = salesAmount * commission_rate
total_salary = base_salary + commission

print(f"Commission rate: {commission_rate}")
print(f"Commission: {commission}")
print(f"Total salary: {total_salary}")
