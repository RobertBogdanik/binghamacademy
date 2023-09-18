e1, e2, e3 = eval(input("Enter three edges: "))

if e1 + e2 > e3 and e1 + e3 > e2 and e2 + e3 > e1:
    print(f"The perimeter is {e1 + e2 + e3}")
else:
    print("The input is invalid")