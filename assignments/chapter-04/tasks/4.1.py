
a, b, c = eval(input("Enter a, b, c: "))

if (b**2 -4*a*c)>0:
    r1 = (-b + (b**2 -4*a*c)**(1/2))/(2*a)
    r2 = (-b - (b**2 -4*a*c)**(1/2))/(2*a)
    print(f"The roots are {r1} and {r2}")
elif (b**2 -4*a*c)<0:
    r1 = (-b + (b**2 -4*a*c)**(1/2))/(2*a)
    print(f"The roots is {r1}")
else:
    print("The equation has no real roots")