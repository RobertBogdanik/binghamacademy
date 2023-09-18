# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!! DO NOT RUN THIS PROGRAM !!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def computeCommission(salesAmount):
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

    return commission

amount = 10000
for i in range(1, 20):
    print(f"{amount}\t\t{computeCommission(amount)}")
    amount += 5000

