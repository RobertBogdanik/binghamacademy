speed, acceleration = eval(input("Enter speed and acceleration: "))

length = (speed**2)/(2*acceleration)

print(f"The minimum runway length for this airplane is {round(length, 3)} meters")
