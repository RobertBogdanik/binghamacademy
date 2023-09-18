weight1, price1 = eval(input("Enter weight and price for package 1: "))
weight2, price2 = eval(input("Enter weight and price for package 2: "))

if (price1/weight1) < (price2/weight2):
    print("Package 2 has the better price.")
elif (price1/weight1) > (price2/weight2):
    print("Package 1 has the better price.")
else:
    print("Two packages have the same price.")